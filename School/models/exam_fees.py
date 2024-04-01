from odoo import fields, models

class exam_fees(models.Model):
    _name = "exam.fees"
    _description = "exam fees details"

    full_name = fields.Char(string="Full Name")
    year = fields.Integer(string="Year")
    roll_no = fields.Integer(string="Roll No")
    standard = fields.Integer(string="Standard")
    section = fields.Char(string="Section")
    contact_no = fields.Integer(string="Contact No")
