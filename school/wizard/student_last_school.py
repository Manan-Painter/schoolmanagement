from odoo import fields, models,api
from datetime import date

class StudentLastSchool(models.Model):
    _name = "student.last.school"
    _description = "Student Last School"


    name = fields.Char(string="Last School")


# model.model
#     res_partner
#         name = manan
#         city
#
# school
#     inherit = res_partner
#     student_name = name = manan
#
#
# abstarct model
#     name
#     message_id
#     city
#
#     sale_order models
#     inherit = abstarct
#     message_id



