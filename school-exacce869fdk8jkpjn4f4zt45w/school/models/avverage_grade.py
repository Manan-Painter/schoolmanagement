from odoo import fields, models ,api,_

class average_grade(models.Model):
    _name = "average.grade"
    _description = "Average Grade"

    student_id = fields.Many2one('school.student','Student Name')
    maths = fields.Integer(string="Maths")
    science = fields.Integer(string="Science")
    chemistry = fields.Integer(string="Chemistry")
    hindi = fields.Integer(string="Hindi")
    gujarati = fields.Integer(string="Gujarati")


    result = fields.Integer(string="Result", compute="_compute_result")

    @api.depends("maths", "science","chemistry","hindi","gujarati")
    def _compute_result(self):
        for rec in self:
            rec.result = (rec.maths + rec.science + rec.chemistry + rec.hindi + rec.gujarati)/5