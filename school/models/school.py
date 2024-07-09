from odoo import fields, models,api,_
from datetime import date

class school(models.Model):
    _name = "school.school"
    _description = "School Details"

    name = fields.Char(string="Name")
    student_id = fields.Many2one('school.student',string='Student')
    teacher_id = fields.Many2one('teacher.student',string='Teacher')

    @api.onchange('student_id')
    def onchange_student_id(self):
        for rec in self:
            return {'domain':{'teacher_id':[('student_id','=',rec.student_id.id)]}}