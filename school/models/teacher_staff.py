from odoo import fields, models,api,_
from datetime import date


class teacher(models.Model):
    _name = "teacher.student"
    _description = "student details"

    heading = fields.Char(string="Heading",readonly=True, default= lambda x: _('Teachers(Staff)'))
    name = fields.Char(string="Name")
    first_name = fields.Char(string="First Name")
    last_name = fields.Char(string="Last Name")
    dob = fields.Date(string="DOB")
    qualification = fields.Char(string="Qualification")
    age = fields.Integer(string="Age",compute='_compute_age')
    lecture = fields.Char(string="Lecture")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender")
    address = fields.Char(string="Address")
    city = fields.Char(string="City")
    contact = fields.Char(string="Contact")
    student_ids = fields.One2many('school.student', 'teacher_id', string='Students')
    attendance_id = fields.Many2one('attendance.teacher','attendance')
    users = fields.Many2one('res.users')
    users_cus = fields.Many2one('res.users')
    remark = fields.Char(string="Teacher Remark", related='attendance_id.remark')
    company_id = fields.Many2one("res.company","Company")
    # student_id = fields.Many2one("school.student","Student")
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
    # students_ids = fields.One2many("school.student","teacher_id",'Student')


    def _compute_age(self):
        for findage in self:
            today = date.today()
            if findage.dob:
                findage.age = today.year - findage.dob.year
            else:
                findage.age = 0

    # def write(self, vals):
    #     if vals.get('gender') == 'male':
    #         self.student_ids = "A"
    #     elif vals.get('gender') == 'female':
    #         self.student_ids = "B"

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('heading') or vals['heading'] == _('New'):
                vals['heading'] = self.env['ir.sequence'].next_by_code('teacher.student') or _('New')
        return super().create(vals_list)

    # teacher_id = fields.Char(string="ID")
    peon_ids = fields.Many2many("peon.student",string="peon")
    def new_method(self):
        pass

    # @api.model
    # def _name_search(self, name='', args=None, operator='ilike', limit=100, name_get_uid=None):
    #     print ("======ar===",args,name)
    #     args = list(args or [])
    #     if name:
    #         args += ['|', ('name', operator, name), ('qualification', operator, name)]
    #     return self._search(args, limit=limit, access_rights_uid=name_get_uid)

    # def name_get(self):
    #     result = []
    #     for account in self:
    #         name = account.code + ' ' + account.name
    #         result.append((account.id, name))
    #     return result

    # def name_get(self):
    #     print("aaaaaaaaa",self)
    #     result = []
    #     print("bbbbbbb",result)
    #     for rec in self:
    #         print("cccccc",rec)
    #         result.append((rec.id, '%s(%s) -- %s' % (rec.name, rec.age, "Test")))
    #         print ("dddddddd",result)
    #     return result