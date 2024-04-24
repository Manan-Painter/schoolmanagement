from odoo import fields, models,api,_


class Res_customer(models.Model):
    _inherit = "res.partner"

    mobile2 = fields.Integer(string="Mobile-2")
    email2 = fields.Char(string="Email-2")
    my_name = fields.Char(string="My_Name")