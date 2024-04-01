from odoo import fields, models

class student_time_table(models.Model):
    _name = "student.time.table"
    _description = "student time table details"

    lecture = fields.Integer(string="Lecture")
    subject = fields.Char(string="Subject")
    time = fields.Datetime(string="Time")
    standard = fields.Char(string="Standard")

