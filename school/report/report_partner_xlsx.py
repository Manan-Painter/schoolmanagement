# Copyright 2017 Creu Blanca
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import models


class PartnerXlsx(models.AbstractModel):
    _name = "report.school.partner_xlsx"
    _inherit = "report.report_xlsx.abstract"
    _description = "Partner XLSX Report"

    def generate_xlsx_report(self, workbook, data, lines):
        # report_name = "Admission Form"
        sheet = workbook.add_worksheet("Admission Report")
        # title = workbook.add_format({'bold': True, 'align': 'center', 'font_size': 20, 'bg_color': 'blue', 'border': True})
        title = workbook.add_format({
            'bold': True,
            'align': 'center',
            'font_size': 20,
            'bg_color': 'blue',  # Background color
            'font_color': 'white',  # Font color
            'border': True
        })
        header_row_style = workbook.add_format({'bold': True, 'align': 'center', 'border': True})
        data_row_style = workbook.add_format({'align': 'center'})

        sheet.merge_range('A1:F1', 'Admission Report', title)
        row = 3
        col = 0



        sheet.set_column(0, 0, 50)  # Column A (Name) width
        sheet.set_column(1, 1, 15)  # Column B (Standard) width
        sheet.set_column(2, 2, 15)  # Column C (Medium) width
        sheet.set_column(3, 3, 30)  # Column D (Address) width
        sheet.set_column(4, 4, 20)  # Column E (Contact) width
        sheet.set_column(5, 5, 20)  # Column F (Extra column, if needed) width

        sheet.write(row, col, 'Name', header_row_style)
        sheet.write(row, col + 1, 'Standard', header_row_style)
        sheet.write(row, col + 2, 'Medium', header_row_style)
        sheet.write(row, col + 3, 'Address', header_row_style)
        sheet.write(row, col + 4, 'Contact', header_row_style)
        row += 2
        sheet.write(row, col, lines.name, data_row_style)
        sheet.write(row, col + 1, lines.std, data_row_style)
        sheet.write(row, col + 2, lines.medium, data_row_style)
        sheet.write(row, col + 3, lines.address, data_row_style)
        sheet.write(row, col + 4, lines.contact, data_row_style)
        row += 1





