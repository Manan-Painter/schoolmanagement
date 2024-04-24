from odoo import fields, models

class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    student_id = fields.Many2one("school.student", string="Student")



class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    student_id = fields.Many2one("school.student", string="Student")