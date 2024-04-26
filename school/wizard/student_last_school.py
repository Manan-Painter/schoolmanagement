from odoo import fields, models,api
from datetime import date

class StudentLastSchool(models.Model):
    _name = "student.last.school"
    _description = "Student Last School"


    name = fields.Char(string="Last School")

