from odoo import fields, models

class bus_fees(models.Model):
    _name = "bus.fees"
    _description = "semester fees details"

    name = fields.Char(string="Name")
    full_name = fields.Char(string="Full Name")
    year = fields.Integer(string="Year")
    roll_no = fields.Integer(string="Roll No")
    standard = fields.Integer(string="Standard")
    section = fields.Char(string="Section")
    contact_no = fields.Integer(string="Contact No")
    student_id = fields.Many2one('school.student', string='Student')
    city = fields.Char(string="City", related='student_id.city')