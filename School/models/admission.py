from odoo import fields, models

class admission(models.Model):
    _name = "admission.student"
    _description = "student details"

    first_name = fields.Char(string="First Name")
    last_name = fields.Char(string="Last Name")
    father_name = fields.Char(string="Father Name")
    mother_name = fields.Char(string="Mother Name")
    last_standard = fields.Integer(string="Last Standard")
    current_standard = fields.Integer(string="Current Standard")
    date_of_birth = fields.Date(string="Date Of Birth")
    student_age = fields.Char(string="Student Age")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender")
    address = fields.Char(string="Address")
    city = fields.Char(string="City")
    contact = fields.Char(string="Contact")