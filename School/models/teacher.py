from odoo import fields, models,api

class teacher(models.Model):
    _name = "teacher.student"
    _description = "student details"

    name = fields.Char(string="Name")
    first_name = fields.Char(string="First Name")
    last_name = fields.Char(string="Last Name")
    dob = fields.Date(string="DOB")
    qualification = fields.Char(string="Qualification")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender")
    address = fields.Char(string="Address")
    city = fields.Char(string="City")
    contact = fields.Char(string="Contact")
    student_ids = fields.One2many('school.student', 'teacher_id', string='Students')
    attendance_id = fields.Many2one('attendance.teacher','attendance')
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