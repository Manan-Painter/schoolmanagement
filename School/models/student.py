from odoo import fields, models

class student(models.Model):
    _name = "school.student"
    _description = "student details"

    first_name = fields.Char(string="First Name")
    last_name = fields.Char(string="Last Name")
    standard = fields.Char(string="Standard")
    date_of_birth = fields.Date(string="Date Of Birth")
    student_age = fields.Char(string="Student Age")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender")
    address = fields.Char(string="Address")
    city = fields.Char(string="City")
    contact = fields.Char(string="Contact")
    teacher_id = fields.Many2one('teacher.student', string='Teacher')
    partner_id = fields.Many2one('res.partner', string='partner')
    qualification = fields.Char(string="Teacher Qualification", related='teacher_id.qualification')