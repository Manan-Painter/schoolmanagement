from odoo import api, fields, models

class SaleOrderWizard(models.TransientModel):
    _name = 'sale.order.register.wizard'

    sale_order_ids = fields.Many2many('sale.order', string='Sale_Order_Register')
    # order_lines = fields.One2many('sale.order','')


