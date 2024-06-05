from odoo import api, fields, models

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_register_payment(self):
        self.ensure_one()
        return {
            'name': 'Register Payment',
            'type': 'ir.actions.act_window',
            'res_model': 'account.payment',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_partner_id': self.partner_id.id,
                'default_amount': self.amount_total,
                'default_payment_type': 'inbound',
                'default_partner_type': 'customer',
                'default_sale_order_ids': [(6, 0, [self.id])],
            },
        }
