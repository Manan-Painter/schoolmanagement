from odoo import fields, models

class assignment(models.Model):
    _name = "assignment.student"
    _description = "assignment"

    student_name = fields.Char(string="Student Name")
    year = fields.Integer(string="Year")
    section = fields.Char(string="Section")
    standard = fields.Integer(string="Standard")
    roll_no = fields.Integer(string="Roll No")
    date = fields.Date(string="Date")
    subject = fields.Char(string="Subject")