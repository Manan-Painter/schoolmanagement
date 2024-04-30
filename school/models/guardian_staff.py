from odoo import fields, models,api,_
from datetime import date


class guardian(models.Model):
    _name = "guardian.student"
    _description = "guardian details"

    heading = fields.Char('Heading', copy=False, readonly=True, default= lambda x: ('Guardian(Staff)'))
    name = fields.Char(string="Name")
    first_name = fields.Char(string="First Name")
    last_name = fields.Char(string="Last Name")
    dob = fields.Date(string="DOB")
    age = fields.Char(string="age",compute='_compute_age')
    work = fields.Char(string="Work")
    qualification = fields.Char(string="Qualification")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender")
    address = fields.Char(string="Address")
    city = fields.Char(string="City")
    contact = fields.Char(string="Contact")
    guardian_ids = fields.One2many('attendance.guardian','guardian_id',string="Guardian")
    state = fields.Selection(selection=[
        ('draft', 'Draft'),
        ('in_Consultation', 'In Consultation'),
        ('done', 'Done'),
        ('cancel', 'Cancelled')], default='draft', string='Status', required='True')
    priority = fields.Selection(selection=[
        ('0', 'Normal'),
        ('1', 'Low'),
        ('2', 'High'),
        ('3', 'Very High')], string='Priority', required='True')

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
            if not vals.get('heading') or vals['heading'] == _('New'):
                vals['heading'] = self.env['ir.sequence'].next_by_code('guardian.student') or _('New')
        return super().create(vals_list)

    def write(self, vals):
        if vals.get('gender') == 'male':
            self.qualification = "BCA"
        elif vals.get('gender') == 'female':
            self.qualification = "BSC"