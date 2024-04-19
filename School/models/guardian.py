from odoo import fields, models,api,_
from datetime import date


class guardian(models.Model):
    _name = "guardian.student"
    _description = "guardian details"

    name = fields.Char(string="Name")
    first_name = fields.Char(string="First Name")
    last_name = fields.Char(string="Last Name")
    dob = fields.Date(string="DOB")
    age = fields.Char(string="age",compute='_compute_age')
    qualification = fields.Char(string="Qualification")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender")
    address = fields.Char(string="Address")
    city = fields.Char(string="City")
    contact = fields.Char(string="Contact")
    guardian_ids = fields.One2many('attendance.guardian','guardian_id',string="Guardian")

    def _compute_age(self):
        for findage in self:
            today = date.today()
            if findage.dob:
                findage.age = today.year - findage.dob.year
            else:
                findage.age = 0

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('name') or vals['name'] == _('New'):
                vals['name'] = self.env['ir.sequence'].next_by_code('guardian.student') or _('New')
        return super().create(vals_list)

    def write(self, vals):
        if vals.get('gender') == 'male':
            self.qualification = "BCA"
        elif vals.get('gender') == 'female':
            self.qualification = "BSC"