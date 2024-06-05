from odoo import api, fields, models, _


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_register_payment(self):
        self.ensure_one()

        # Ensure the sale order is confirmed
        if self.state not in ['sale', 'done']:
            raise UserError(_("You can only register payment for confirmed or done sale orders."))

        # Ensure there is at least one invoice
        invoices = self.invoice_ids.filtered(lambda inv: inv.state == 'posted')
        if not invoices:
            raise UserError(_("There are no posted invoices related to this sale order."))

        # For simplicity, we consider only the first posted invoice
        invoice = invoices[0]

        return {
            'name': 'Register Payment',
            'type': 'ir.actions.act_window',
            'res_model': 'account.payment.register',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_partner_id': self.partner_id.id,
                'default_amount': invoice.amount_residual,
                'default_payment_type': 'inbound',
                'default_partner_type': 'customer',
                'active_model': 'account.move',
                'active_ids': [invoice.id],
                'active_id': invoice.id,
            },
        }
