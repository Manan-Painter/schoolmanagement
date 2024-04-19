from odoo import fields, models,api,_
from datetime import date


class teacher(models.Model):
    _name = "teacher.student"
    _description = "student details"

    name = fields.Char(string="Name",readonly=True, default= lambda x: _('New'))
    first_name = fields.Char(string="First Name")
    last_name = fields.Char(string="Last Name")
    dob = fields.Date(string="DOB")
    qualification = fields.Char(string="Qualification")
    age = fields.Integer(string="Age",compute='_compute_age')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender")
    address = fields.Char(string="Address")
    city = fields.Char(string="City")
    contact = fields.Char(string="Contact")
    student_ids = fields.One2many('school.student', 'teacher_id', string='Students')
    attendance_id = fields.Many2one('attendance.teacher','attendance')
    remark = fields.Char(string="Teacher Remark", related='attendance_id.remark')

    def _compute_age(self):
        for findage in self:
            today = date.today()
            if findage.dob:
                findage.age = today.year - findage.dob.year
            else:
                findage.age = 0

    def write(self, vals):
        if vals.get('gender') == 'male':
            self.student_ids = "A"
        elif vals.get('gender') == 'female':
            self.student_ids = "B"

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('name') or vals['name'] == _('New'):
                vals['name'] = self.env['ir.sequence'].next_by_code('teacher.student') or _('New')
        return super().create(vals_list)

    # teacher_id = fields.Char(string="ID")
    peon_ids = fields.Many2many("peon.student",string="peon")
    def new_method(self):
        pass

    @api.model
    def _name_search(self, name='', args=None, operator='ilike', limit=100, name_get_uid=None):
        print ("======ar===",args,name)
        args = list(args or [])
        if name:
            args += ['|', ('name', operator, name), ('qualification', operator, name)]
        return self._search(args, limit=limit, access_rights_uid=name_get_uid)

    def name_get(self):
        print("aaaaaaaaa",self)
        result = []
        print("bbbbbbb",result)
        for rec in self:
            print("cccccc",rec)
            result.append((rec.id, '%s(%s) -- %s' % (rec.first_name, rec.last_name, "Test")))
            print ("dddddddd",result)
        return result