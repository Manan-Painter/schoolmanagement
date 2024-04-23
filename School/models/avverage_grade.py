from odoo import fields, models

class average_grade(models.Model):
    _name = "average.grade"
    _description = "Average Grade"

    student_id = fields.Many2one('school.student','Student Name')
    maths = fields.Integer(string="Maths")
    science = fields.Integer(string="Science")
    chemistry = fields.Integer(string="Chemistry")
    hindi = fields.Integer(string="Hindi")
    gujarati = fields.Integer(string="Gujarati")


