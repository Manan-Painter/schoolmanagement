from odoo import fields, models,api,_


class SaleOrder(models.Model):
    _inherit = "sale.order"

    teacher_id = fields.Many2one("teacher.student", string="Teacher")
