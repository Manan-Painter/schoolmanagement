from odoo import fields, models,api
from datetime import date

class AdmissionCancel(models.Model):
    _name = "admission.cancel"
    _description = "Admission Cancel"

    name = fields.Char(string="Reason")
    wiz_admission_id = fields.Many2one("admission.student", "Admission")

    # def _compute_name(self):
    #     drive_obj = self.env['admission.student'].browse(self._context.get("active_id"))
    #     for rec in self:
    #         rec.name = drive_obj.heading
    # def action_admission_cancel(self):
    #     drive_obj = self.env['admission.student'].browse(self._context.get("active_id"))
    #     drive_obj.cancel_reason = self.name
    #     drive_obj.status = "cancelled"
    #     self.name = drive_obj.heading






