from odoo import models, fields, api

class RegisterPaymentWizard(models.TransientModel):
    _name = 'register.payment'
    _description = 'Register Payment Wizard'

    sale_order_ids = fields.Many2many(
        'sale.order',
        string='Sale Orders'
    )

    product_lines = fields.One2many(
        'register.payment.product.line',
        'wizard_id',
        string='Product Lines'
    )

    @api.model
    def default_get(self, fields_list):
        res = super(RegisterPaymentWizard, self).default_get(fields_list)

        sale_order_ids = self.env.context.get('sale_order_ids', [])
        if 'product_lines' in fields_list and sale_order_ids:
            sale_orders = self.env['sale.order'].browse(sale_order_ids)
            product_lines = []
            for order in sale_orders:
                # Consider adding a domain to filter order lines (e.g., outstanding balance)
                for line in order.order_line:
                    product_lines.append(self.env['register.payment.product.line'].create({
                        'wizard_id': self.id,
                        'product_id': line.product_id.id,
                        'description': line.name,
                        'cost': line.price_unit,
                    }))
            res['product_lines'] = [(6, 0, product_lines.ids)]  # Convert to Odoo one2many format

        return res


class RegisterPaymentProductLine(models.TransientModel):
    _name = 'register.payment.product.line'
    _description = 'Register Payment Product Line'

    wizard_id = fields.Many2one('register.payment', string='Wizard')
    product_id = fields.Many2one('product.product', string='Product')
    description = fields.Text(string='Description')
    cost = fields.Float(string='Cost')


