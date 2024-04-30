from odoo import fields, models,api
from datetime import date

class AdmissionCancel(models.Model):
    _name = "admission.cancel"
    _description = "Admission Cancel"


    reason = fields.Char(string="Reason")
    wiz_admission_id = fields.Many2one("admission.student", "Admission")


    def action_admission_cancel(self):
        drive_obj = self.env['admission.student'].browse(self._context.get("active_id"))
        drive_obj.cancel_reason = self.reason
        drive_obj.status = "cancelled"

