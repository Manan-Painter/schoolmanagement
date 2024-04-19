from odoo import fields, models

class attendance_guardian(models.Model):
    _name = "attendance.guardian"
    _description = "guardian details"

    name = fields.Char(string="Name")
    present = fields.Char(string="Present")
    absent = fields.Char(string="Absent")
    remark = fields.Char(string="Remark")
    start_time = fields.Datetime(string="Start Time")
    end_time = fields.Datetime(string="End Time")
    guardian_id = fields.Many2one('guardian.student', 'Guardian')
    first_name = fields.Char(string="Guardian Name", related='guardian_id.first_name')
