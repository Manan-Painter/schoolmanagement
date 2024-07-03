# your_module/models/sale_order_wizard.py
from odoo import models, fields, api


class SaleOrderPrintWizard(models.TransientModel):
    _name = 'sale.order.print.wizard'
    _description = 'Sale Order Print Wizard'

    def get_report(self):
        return self.env['ir.actions.report'].search([
        ('model', '=', 'sale.order'), ('report_type', '=', 'qweb-pdf')
    ], limit=1)


    print_report = fields.Many2one('ir.actions.report',string='Print_Report',
                                   domain="[('model', '=', 'sale.order'), ('report_type', '=', 'qweb-pdf')],",default=get_report)

    def download_report(self):
        active_id = self.env.context.get('active_id')
        print('-------',self.env.context)
        active_model = self.env.context.get('active_model')

        sale_order = self.env[active_model].browse(active_id)
        report = self.env["ir.actions.report"]._get_report_from_name(
            self.print_report.report_name
        )

        report_action = report.report_action(sale_order)
        report_action.update({"close_on_report_download": True})
        return report_action