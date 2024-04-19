from odoo import fields, models,api,_
from datetime import date


class admission(models.Model):
    _name = "admission.student"
    _description = "student details"


    name = fields.Char('Name', copy=False, readonly=True, default= lambda x: _('New'))
    last_name = fields.Char(string="Last Name")
    father_name = fields.Char(string="Father Name")
    mother_name = fields.Char(string="Mother Name")
    last_standard = fields.Integer(string="Last Standard")
    current_standard = fields.Integer(string="Current Standard")
    date_of_birth = fields.Date(string="Date Of Birth")
    age = fields.Char(string="Student Age",compute='_compute_age')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender")
    address = fields.Char(string="Address")
    city = fields.Char(string="City")
    contact = fields.Char(string="Contact")
    student_ids = fields.One2many('school.student', 'admission_id', string='Students')

    def _compute_age(self):
        for findage in self:
            today = date.today()
            if findage.date_of_birth:
                findage.age = today.year - findage.dob.year
            else:
                findage.age = 0

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('name') or vals['name'] == _('New'):
                vals['name'] = self.env['ir.sequence'].next_by_code('admission.student') or _('New')
        return super().create(vals_list)

    def write(self, vals):
        if vals.get('gender') == 'male':
            self.contact = "1245782356"
        elif vals.get('gender') == 'female':
            self.contact = "2356891256"
        return super().write(vals)