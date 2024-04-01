from odoo import fields, models

class exam_attendance(models.Model):
    _name = "result.student"
    _description = "result"

    student_name = fields.Char(string="Student Name")
    year = fields.Integer(string="Year")
    section = fields.Char(string="Section")
    standard = fields.Integer(string="Standard")
    roll_no = fields.Integer(string="Roll No")
    date = fields.Date(string="Date")
    total_marks = fields.Integer(string="Total Marks")
    percentage =fields.Float(string="Percentage")