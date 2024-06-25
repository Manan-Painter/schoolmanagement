from odoo import fields, models,api,_
from datetime import date

class PriceListReport(models.AbstractModel):
    _name = 'report.price_list_report.price_list_report'
    _inherit = 'report.report_xlsx.partner_xlsx'
    _description = 'Price List Report'
def GetData(self):
    return self.env['price.list.wizard'].data['lines']
def generate_xlsx_report(self, workbook, data, lines):
    datas = self.GetData()