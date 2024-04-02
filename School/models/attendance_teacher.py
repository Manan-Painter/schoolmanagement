from odoo import fields, models

class attendance_teacher(models.Model):
    _name = "attendance.teacher"
    _description = "student details"

    name = fields.Char(string="Name")
    present = fields.Char(string="Present")
    absent = fields.Char(string="Absent")
    remark = fields.Char(string="Remark")
    start_time = fields.Datetime(string="Start Time")
    end_time = fields.Datetime(string="End Time")
    teacher_ids = fields.One2many('teacher.student', 'attendance_id', 'Teacher')