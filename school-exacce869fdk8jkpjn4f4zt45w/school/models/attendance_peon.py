from odoo import fields, models

class attendance_peon(models.Model):
    _name = "attendance.peon"
    _description = "peon details"

    name = fields.Char(string="Name")
    present = fields.Char(string="Present")
    absent = fields.Char(string="Absent")
    remark = fields.Char(string="Remark")
    start_time = fields.Datetime(string="Start Time")
    end_time = fields.Datetime(string="End Time")
    peon_id = fields.Many2one('peon.student', 'Peon')

    first_name = fields.Char(string="First Name", related='peon_id.first_name')
