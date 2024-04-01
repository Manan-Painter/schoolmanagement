from odoo import fields, models


class teacher_time_table(models.Model):
    _name = "teacher_time_table"
    _description = "teacher time table details"

    teacher_name = fields.Char(string="Teacher_Name")
    lecture = fields.Integer(string="Lecture")
    subject = fields.Char(string="Subject")
    time = fields.Datetime(string="Time")
    standard = fields.Char(string="Standard")

