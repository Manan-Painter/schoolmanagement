from odoo import fields, models,api,_


class Rescustomer(models.Model):
    _inherit = "product.template"

    inactive = fields.Boolean(string="In Active")
