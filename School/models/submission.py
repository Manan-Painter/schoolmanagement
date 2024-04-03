from odoo import fields, models

class home_work(models.Model):
    _name = "home.work.student"
    _description = "Home Work"

    name = fields.Char(string="Name")
    student_name = fields.Char(string="Student Name")
    year = fields.Integer(string="Year")
    section = fields.Char(string="Section")
    standard = fields.Integer(string="Standard")
    roll_no = fields.Integer(string="Roll No")
    date = fields.Date(string="Date")
    subject = fields.Char(string="Subject")
    form_ids = fields.One2many('exam.form','submission_id','Exam_Form_id')
    experience = fields.Char(string="experience")
