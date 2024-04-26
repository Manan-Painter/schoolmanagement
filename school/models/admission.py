from odoo import fields, models,api,_
from datetime import date


class admission(models.Model):
    _name = "admission.student"
    _description = "student details"


    heading = fields.Char('Heading', copy=False, readonly=True, default= lambda x: _('Admission Form'))
    name = fields.Char(string="Name",require='True')
    academic_year = fields.Char(string="Academic Year")
    admission_date = fields.Date(string="Admission Date")
    std = fields.Integer(string="Class")
    second_language = fields.Char(string="Second Language")
    medium = fields.Char(string="Medium")
    date_of_birth = fields.Date(string="Date Of Birth")
    age = fields.Char(string="Student Age",compute='_compute_age')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender")
    address = fields.Char(string="Address")
    city = fields.Char(string="City")
    contact = fields.Char(string="Contact")
    # student_ids = fields.One2many('school.student', 'admission_id', string='Students')

    def _compute_age(self):
        for findage in self:
            today = date.today()
            if findage.date_of_birth:
                findage.age = today.year - findage.date_of_birth.year
            else:
                findage.age = 0

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('heading') or vals['heading'] == _('New'):
                vals['heading'] = self.env['ir.sequence'].next_by_code('admission.student') or _('New')
        return super().create(vals_list)

    def write(self, vals):
        if vals.get('gender') == 'male':
            self.contact = "1245782356"
        elif vals.get('gender') == 'female':
            self.contact = "2356891256"
        return super().write(vals)