from odoo import fields, models,api
from datetime import date

class AdmissionCancel(models.Model):
    _name = "admission.cancel"
    _description = "Admission Cancel"


    reason = fields.Char(string="Reason")
    wiz_admission_id = fields.Many2one("admission.student", "Admission")

