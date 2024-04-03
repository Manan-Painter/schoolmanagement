from odoo import fields, models

class teacher(models.Model):
    _name = "peon.student"
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
    peon_ids = fields.One2many('attendance.peon','peon_id',string="Peon")
    teacher_ids = fields.Many2many("teacher.student", "peon_teacher_rel", string="Teacher")
