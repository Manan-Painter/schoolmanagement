from odoo import fields, models,api,_


class SaleOrder(models.Model):
    _inherit = "sale.order"

    teacher_id = fields.Many2one("teacher.student", string="Teacher")

class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    line_teacher_id = fields.Many2one(related="order_id.teacher_id", string="Teacher")