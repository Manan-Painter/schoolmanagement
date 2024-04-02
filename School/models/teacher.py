from odoo import fields, models

class teacher(models.Model):
    _name = "teacher.student"
    _description = "student details"

    name = fields.Char(string="Name")
    first_name = fields.Char(string="First Name")
    last_name = fields.Char(string="Last Name")
    dob = fields.Date(string="DOB")
    qualification = fields.Char(string="Qualification")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender")
    address = fields.Char(string="Address")
    city = fields.Char(string="City")
    contact = fields.Char(string="Contact")
    student_ids = fields.One2many('school.student', 'teacher_id', string='Students')

    def new_method(self):
        pass