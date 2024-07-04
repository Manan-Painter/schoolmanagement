from odoo import fields, models,api,_
from datetime import date


class school_student_list(models.Model):
    _name = "school.student.list"
    _description = "school.student.list"


    admission_list_id = fields.Many2one("admission.student")
    student_id = fields.Many2one('school.student', string='Student')
    age = fields.Char(related="student_id.age")
    stu_list_registration_fees = fields.Float("Registration Fees")

    @api.onchange('student_id')
    def onchange_student(self):
        if self.student_id:
            self.stu_list_registration_fees = self.student_id.registration_fees

    # @api.onchange("student_id")
    # def student_id(self):
    #     self.stu_list_registration_fees = self.student_id.registration_fees

class admission(models.Model):
    _name = "admission.student"
    _description = "student details"
    _inherit = ['mail.thread', 'mail.activity.mixin','portal.mixin']

    # def _get_student_data(self):
    #     domain = "[('standard', '=', '12')]"
    #     return domain

    heading = fields.Char('Heading', copy=False, readonly=True, default= lambda x: _('Admission Form'))
    name = fields.Char(string="Name")
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
    state = fields.Selection(selection=[
        ('draft', 'Draft'),
        ('in_Consultation', 'In Consultation'),
        ('done', 'Done'),
        ('cancel', 'Cancelled')], default='draft', string='Status', required='True')
    priority = fields.Selection(selection=[
        ('0', 'Normal'),
        ('1', 'Low'),
        ('2', 'High'),
        ('3', 'Very High')], string='Priority')
    student_ids = fields.One2many('school.student', 'admission_id', string='Students')
    student_id = fields.Many2one('school.student' ,string='Student')
    student_list_ids = fields.One2many('school.student.list', 'admission_list_id', string='Students')
    # domain = "[('standard', '=', '12'))]"
    # domain = _get_student_data

    def _compute_access_url(self):
        super(admission, self)._compute_access_url()
        for add in self:
            add.access_url = '/my/admission/%s' % (add.id)

    def _get_report_base_filename(self):
        self.ensure_one()
        return 'Admission -%s' % (self.name)

    def action_approve_admission(self):
        for rec in self:
            rec.state = "in_Consultation"

    def action_cancel_admission(self):
        for rec in self:
            rec.state = "cancel"

    def _compute_age(self):
        for findage in self:
            today = date.today()
            if findage.date_of_birth:
                findage.age = today.year - findage.date_of_birth.year
            else:
                findage.age = 0

    @api.model_create_multi
    def create(self, vals_list):
        res = super().create(vals_list)
        for vals in vals_list:
            if not vals.get('heading') or vals['heading'] == _('New'):
                vals['heading'] = self.env['ir.sequence'].next_by_code('admission.student') or _('New')
        books_student_vals = {
            "name": res.name
        }
        books_id = self.env["books.books"].create(books_student_vals)
        return res

    def write(self, vals):
        res = super().write(vals)
        if vals.get('gender') == 'male':
            self.contact = "1245782356"
        elif vals.get('gender') == 'female':
            self.contact = "2356891256"
        if self.std <= 5:
            for line in self.student_list_ids:
                print ("lllll",line,line.student_id.name)
                # line.stu_list_registration_fees = 250
                line.update({
                    "stu_list_registration_fees":250,
                })
                # self.update({"student_list_ids" : [(1, line.id, {
                #     "stu_list_registration_fees": 300,
                # })]})
        return res

    def action_approve_admission_email_send(self):
        """ Opens a wizard to compose an email, with relevant mail template loaded by default """
        self.ensure_one()
        ir_model_data = self.env['ir.model.data']
        try:
            template_id = ir_model_data._xmlid_lookup('school.email_template_edi_admission')[2]
        except ValueError:
            template_id = False

        try:
            compose_form_id = ir_model_data._xmlid_lookup('mail.email_compose_message_wizard_form')[2]
        except ValueError:
            compose_form_id = False

        ctx = {
            'default_model': 'admission.student',
            'default_res_id': self.id,
            'default_use_template': bool(template_id),
            'default_template_id': template_id,
            'default_composition_mode': 'comment',
            'mark_so_as_sent': True,
            'force_email': True,
        }
        return {
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'mail.compose.message',
            'views': [(compose_form_id, 'form')],
            'view_id': compose_form_id,
            'target': 'new',
            'context': ctx,
        }

