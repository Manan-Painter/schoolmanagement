from odoo import fields, models, api,_
import logging

_logger = logging.getLogger(__name__)

from datetime import date
class student(models.Model):
    _name = "school.student"
    _description = "student details"
    _inherit = ['mail.thread', 'mail.activity.mixin','portal.mixin']
    # _rec_name = 'gender'

    heading = fields.Char('Heading', copy=False, readonly=True, default= lambda x: ('Student List'))
    teacher = fields.Char(string="Teacher")
    name = fields.Char('Name')
    # first_name = fields.Char(sring="first_name")
    standard = fields.Integer(string="Standard")
    school_standard = fields.Integer(string="Standard")
    date_of_birth = fields.Date(string="Date Of Birth")
    age = fields.Char(string="Student Age", compute="_compute_age")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender", default="female")
    address = fields.Char(string="Address")
    city = fields.Char(string="City")
    contact = fields.Char(string="Contact")
    teacher_id = fields.Many2one('teacher.student', string='Teacher')
    school_id = fields.Many2one('school.school',string='School')
    admission_id = fields.Many2one('admission.student', string='Admission')
    partner_id = fields.Many2one('res.users',related='user_id.partner_id')
    company_id = fields.Many2one("res.company",  default=lambda self: self.env.company)
    currency_id = fields.Many2one(
        related='company_id.currency_id',
        store=True, precompute=True, ondelete="restrict")
    stud_phone = fields.Char(related="company_id.phone")
    registration_fees = fields.Float()
    tution_fees = fields.Float()
    total_fees = fields.Monetary("Total Fees", store=True, compute="_compute_total_fees")
    state = fields.Selection(selection=[
        ('draft', 'Draft'),
        ('in_Consultation', 'In Consultation'),
        ('done', 'Done'),
        ('cancel', 'Cancelled')],default='draft', string='Status',required='True')
    priority = fields.Selection(selection=[
        ('0', 'Normal'),
        ('1', 'Low'),
        ('2', 'High'),
        ('3', 'Very High')], string='Priority')
    donation_fees = fields.Float("Donation")
    grade_ids = fields.One2many('average.grade','student_id',string="Grade")
    issues = fields.Html(string="Issue")
    company_id = fields.Many2one('res.company','Company')
    # teacher_id = fields.Many2one("teacher.student", "teacher")
    created_user_id = fields.Many2one('res.users' , string="Created User")
    partner_id = fields.Many2one('res.partner',related='created_user_id.partner_id',     string='Related User')

    @api.onchange('teacher_id')
    def onchange_teacher_id(self):
        for rec in self:
            return {'domain': {'school_id': [('teacher_id', '=', rec.teacher_id.id)]}}

    @api.onchange('school_id')
    def onchange_school_id(self):
        for rec in self:
            return {'domain': {'teacher_id': [('school_id', '=', rec.school_id.id)]}}


    # _sql_constraints = [
    #     ('number_uniq', 'CHECK(school_standard >= 10)', 'Please enter a valid Standard  .'),
    # ]
    # @api.constrains('standard')
    # def _check_std(self):
    #     for std in self:
    #         if int(std.standard) >= 10:
    #             raise ValidationError("Plz Enter Primary standard")

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            print ("=====vals==",vals.get('heading'),self.env['ir.sequence'].next_by_code('school.student'))
            if vals.get('heading', 'New') == 'New':
                vals['heading'] = self.env['ir.sequence'].next_by_code('school.student') or '/'
        return super().create(vals_list)

    def _compute_access_url(self):
        super(student, self)._compute_access_url()
        for stud in self:
            stud.access_url = '/my/students/%s' % (stud.id)

    def _get_report_base_filename(self):
        self.ensure_one()
        return 'Student -%s' % (self.name)

    @api.depends("registration_fees", "tution_fees")
    def _compute_total_fees(self):
        for rec in self:
            rec.total_fees = rec.registration_fees + rec.tution_fees

    def action_approve_student(self):
        for rec in self:
            rec.state = "in_Consultation"

    def action_cancel_student(self):
        for rec in self:
            rec.state = "cancel"

    def _compute_age(self):
        for findage in self:
            today = date.today()
            if findage.date_of_birth:
                findage.age = today.year - findage.date_of_birth.year
            else:
                findage.age = 0

    def write(self, vals):
        if vals.get('gender') == 'male':
            self.city ="khambhat"
            self.contact = "A"
        elif vals.get('gender') == 'female':
            self.contact = "B"
        if vals.get('name'):
            user_id = self.env['res.users'].search([('id','=', self.created_user_id.id)])
            if user_id:
                user_id.name = vals.get('name')
            print ("uuuuu",user_id)
        return super().write(vals)

    @api.model
    def _name_search(self, name='', args=None, operator='ilike', limit=100, name_get_uid=None):
        args = list(args or [])
        if name:
            args += ['|', ('name', operator, name), ('name', operator, name)]
        return self._search(args, limit=limit, access_rights_uid=name_get_uid)

    def button_save(self):
        print("button clicked")

    def action_open_list(self):
        return {
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'student.last.school',
            'target': 'new',
        }

    def action_approve_student_email_send(self):
        """ Opens a wizard to compose an email, with relevant mail template loaded by default """
        self.ensure_one()
        ir_model_data = self.env['ir.model.data']
        try:
            template_id = ir_model_data._xmlid_lookup('school.email_template_edi_student')[2]
        except ValueError:
            template_id = False

        try:
            compose_form_id = ir_model_data._xmlid_lookup('mail.email_compose_message_wizard_form')[2]
        except ValueError:
            compose_form_id = False

        ctx = {
            'default_model': 'school.student',
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