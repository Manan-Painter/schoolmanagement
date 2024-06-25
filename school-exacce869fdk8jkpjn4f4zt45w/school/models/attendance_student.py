from odoo import fields, models

class attendance_student(models.Model):
    _name = "attendance.student.student"
    _description = "student details"

    name = fields.Char(string="Name")
    present = fields.Char(string="Present")
    absent = fields.Char(string="Absent")
    remark = fields.Char(string="Remark")
    start_time = fields.Datetime(string="Start Time")
    end_time = fields.Datetime(string="End Time")
    type_student = fields.Selection(
        [('clever', 'Clever'), ('medium', 'Medium'), ('low', 'Low')], default="low", string='Student Type')
    teacher_id = fields.Many2one("teacher.student")
    company_id = fields.Many2one("res.company", "Company")

