from odoo import api, fields, models, _
from odoo.exceptions import UserError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    can_register_payment = fields.Boolean(
        string='Can Register Payment',
        compute='_compute_can_register_payment',
        store=True
    )

    @api.depends('state', 'invoice_ids.payment_state')
    def _compute_can_register_payment(self):
        for order in self:
            order.can_register_payment = (
                order.state in ['sale', 'done'] and
                any(invoice.payment_state == 'not_paid' for invoice in order.invoice_ids)
            )

    def action_register_payment(self):
        self.ensure_one()

        # Ensure the sale order is confirmed
        if self.state not in ['sale', 'done']:
            raise UserError(_("You can only register payment for confirmed or done sale orders."))

        # Ensure there is at least one invoice
        invoices = self.invoice_ids.filtered(lambda inv: inv.state == 'posted')
        if not invoices:
            raise UserError(_("There are no posted invoices related to this sale order."))

        # Calculate the total amount due for all posted invoices
        total_amount_due = sum(invoice.amount_residual for invoice in invoices)

        return {
            'name': 'Register Payment',
            'type': 'ir.actions.act_window',
            'res_model': 'account.payment.register',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_partner_id': self.partner_id.id,
                'default_amount': total_amount_due,
                'default_payment_type': 'inbound',
                'default_partner_type': 'customer',
                'active_model': 'account.move',
                'active_ids': invoices.ids,  # Pass all invoice IDs
                'active_id': invoices[0].id,  # Use the first invoice ID for the form context
            },
        }


    def action_open_print_wizard(self):
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'sale.order.print.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_sale_order_id': self.id,
            }
        }