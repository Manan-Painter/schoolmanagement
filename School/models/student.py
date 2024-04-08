from odoo import fields, models, api, _
from odoo.exceptions import ValidationError

class student(models.Model):
    _name = "school.student"
    _description = "student details"

    name = fields.Char('Reference', copy=False, readonly=True, default=lambda x: _('New'))
    first_name = fields.Char(string="First Name")
    last_name = fields.Char(string="Last Name")
    standard = fields.Char(string="Standard")
    date_of_birth = fields.Date(string="Date Of Birth")
    student_age = fields.Char(string="Student Age", default="10")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender", default="female")
    address = fields.Char(string="Address")
    city = fields.Char(string="City")
    contact = fields.Char(string="Contact")
    teacher_id = fields.Many2one('teacher.student', string='Teacher')
    partner_id = fields.Many2one('res.partner', string='partner')
    qualification = fields.Char(string="Teacher Qualification", related='teacher_id.qualification')
    student_ids = fields.One2many('bus.fees', 'student_id', string='Students')

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

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('name') or vals['name'] == _('New'):
                vals['name'] = self.env['ir.sequence'].next_by_code('school.student') or _('New')
                vals['last_name'] = "Maheshwari"
        return super().create(vals_list)

    def write(self, vals):
        if vals.get('gender') == 'male':
            self.city =" khambhat"
            self.contact = "A"
        elif vals.get('gender') == 'female':
            self.contact = "B"
        return super().write(vals)
    #
    # def unlink(self):
    #     for rec in self:
    #         if rec.gender == 'male':
    #             raise ValidationError('You can not Delete <%s>' % rec.first_name)
    #     return super(student, self).unlink()