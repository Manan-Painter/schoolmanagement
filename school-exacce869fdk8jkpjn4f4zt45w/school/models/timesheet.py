from odoo import fields, models, api, _
from odoo.exceptions import ValidationError
from datetime import date, datetime, timedelta

class Timesheet(models.Model):
    _inherit = 'account.analytic.line'

    @api.constrains('date')
    def _compute_timesheet_date(self):
        today = fields.Date.today()
        date = today - timedelta(days=5)

        for rec in self:
            if rec.date < date:
                raise ValidationError(f"Action must be applied within the last 5 days. "
                                          f"Provided date: {rec.date.strftime('%Y-%m-%d')}")
