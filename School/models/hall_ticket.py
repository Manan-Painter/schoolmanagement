from odoo import fields, models

class hall_ticket(models.Model):
    _name = "hall.ticket"
    _description = "hall ticket details"

    student_name = fields.Char(string="Student Name")
    year = fields.Integer(string="Year")
    section = fields.Char(string="Section")
    standard = fields.Integer(string="Standard")
    roll_no = fields.Integer(string="Roll No")
    date = fields.Date(string="Date")