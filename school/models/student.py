from odoo import fields, models, api, _
from datetime import date
from odoo.exceptions import ValidationError

class student(models.Model):
    _name = "school.student"
    _description = "student details"

    name = fields.Char('Name')
    # first_name = fields.Char(string="First Name")
    last_name = fields.Char(string="Last Name")
    standard = fields.Char(string="Standard")
    date_of_birth = fields.Date(string="Date Of Birth")
    age = fields.Char(string="Student Age")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender", default="female")
    address = fields.Char(string="Address")
    city = fields.Char(string="City")
    contact = fields.Char(string="Contact")
    teacher_id = fields.Many2one('teacher.student', string='Teacher')
    # partner_id = fields.Many2one('res.partner', string='partner')
    qualification = fields.Char(string="Teacher Qualification", related='teacher_id.qualification')
    admission_id = fields.Many2one('admission.student', string='Admission')
    # average_ids = fields.One2many('average.grade','student_id',string="Average Grade")
    # student_ids = fields.One2many('bus.fees', 'student_id', string='Students')
    partner_id = fields.Many2one("res.partner", string="Partner")

    company_id = fields.Many2one("res.company",  default=lambda self: self.env.company)
    currency_id = fields.Many2one(
        related='company_id.currency_id',
        store=True, precompute=True, ondelete="restrict")
    stud_phone = fields.Char(related="company_id.phone")
    registration_fees = fields.Float()
    tution_fees = fields.Float()
    total_fees = fields.Monetary("Total Fees", store=True, compute="_compute_total_fees")

    donation_fees = fields.Float("Donation")

    @api.depends("registration_fees", "tution_fees")
    def _compute_total_fees(self):
        for rec in self:
            print("<<<<<<<<<<<<")
            rec.total_fees = rec.registration_fees + rec.tution_fees


    # def _compute_age(self):
    #     for findage in self:
    #         today = date.today()
    #         if findage.date_of_birth:
    #             findage.age = today.year - findage.date_of_birth.year
    #         else:
    #             findage.age = 0
    #
    # @api.model_create_multi
    # def create(self, vals_list):
    #     res = super(student, self).create(vals_list)
    #     # if res.gender == 'male':
    #     #     res.standard = "01"
    #     addmission_student = {
    #         "first_name" : res.first_name,
    #     }
    #     self.env["admission.student"].create(addmission_student)
    #     return res

    # @api.model_create_multi
    # def create(self, vals_list):
    #     for vals in vals_list:
    #         if not vals.get('name') or vals['name'] == _('New'):
    #             vals['name'] = self.env['ir.sequence'].next_by_code('school.student') or _('New')
    #             vals['last_name'] = "Maheshwari"
    #     return super().create(vals_list)

    # @api.model_create_multi
    # def create(self, vals_list):
    #     for vals in vals_list:
    #         if not vals.get('name') or vals['name'] == _('New'):
    #             vals['name'] = self.first_name
    #     return super().create(vals_list)

    # def write(self, vals):
    #     if vals.get('gender') == 'male':
    #         self.city ="khambhat"
    #         self.contact = "A"
    #     elif vals.get('gender') == 'female':
    #         self.contact = "B"
    #     return super().write(vals)
    # #
    # def unlink(self):
    #     for rec in self:
    #         if rec.gender == 'male':
    #             raise ValidationError('You can not Delete <%s>' % rec.first_name)
    #     return super(student, self).unlink()

    @api.model
    def _name_search(self, name='', args=None, operator='ilike', limit=100, name_get_uid=None):
        print("======ar===", args, name)
        args = list(args or [])
        if name:
            args += ['|', ('name', operator, name), ('first_name', operator, name)]
        return self._search(args, limit=limit, access_rights_uid=name_get_uid)

    def action_test(self):
        print("button clicked")