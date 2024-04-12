from odoo import fields, models, api

class exam_attendance(models.Model):
    _name = "result.student"
    _description = "result"

    student_name = fields.Char(string="Student Name")
    year = fields.Integer(string="Year")
    section = fields.Char(string="Section")
    standard = fields.Integer(string="Standard")
    roll_no = fields.Integer(string="Roll No")
    date = fields.Date(string="Date")
    total_marks = fields.Integer(string="Total Marks")
    percentage =fields.Float(string="Percentage")


class BaseClass(models.Model):
    _name = "base.model"
    _description = "Base Class"

    name = fields.Char("Base Name")
    first_name = fields.Char("First Name")
    partner_id = fields.Many2one("res.partner", "Partner")
    company_id = fields.Many2one("res.company", "Company")
    value1 = fields.Integer("Value 1")
    value2 = fields.Integer("Value 2")
    total = fields.Integer(compute="_get_total", string="Total")

    def _get_total(self):
        for rec in self:
            rec.total = rec.value1 + rec.value2
            print ("=========total======",rec.total)


class SubClass(models.Model):
    _inherit = "base.model"
    _description = "Base Class"

    last_name = fields.Char("Last Name")
    sub_city = fields.Char("City")

    @api.onchange('last_name', "partner_id")
    def _onchange_last_name(self):
        for rec in self:
            rec.first_name = rec.last_name
            rec.sub_city = rec.partner_id.city
            rec._get_total()