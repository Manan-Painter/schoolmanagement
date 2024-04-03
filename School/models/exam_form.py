from odoo import fields, models

class exam_form(models.Model):
    _name = "exam.form"
    _description = "exam fees details"

    name = fields.Char(string="name")
    student_name = fields.Char(string="Student Name")
    year = fields.Integer(string="Year")
    section = fields.Char(string="Section")
    standard = fields.Integer(string="Standard")
    roll_no = fields.Integer(string="Roll No")
    date = fields.Date(string="Date")
    submission_id = fields.Many2one('home.work.student', 'Submission')
    experience = fields.Char(string="Experiance",related='submission_id.experience')