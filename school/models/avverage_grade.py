from odoo import fields, models ,api,_

class average_grade(models.Model):
    _name = "average.grade"
    _description = "Average Grade"

    heading = fields.Char('Heading', copy=False, readonly=True, default=lambda x: _('Grade Form'))
    student_id = fields.Many2one('school.student','Student Name')
    maths = fields.Integer(string="Maths")
    science = fields.Integer(string="Science")
    chemistry = fields.Integer(string="Chemistry")
    hindi = fields.Integer(string="Hindi")
    gujarati = fields.Integer(string="Gujarati")
    teacher_id = fields.Many2one('teacher.student', string='Teacher')
    created_user_id = fields.Many2one('res.users', string="Created User")


    result = fields.Integer(string="Result", compute="_compute_result")

    @api.depends("maths", "science","chemistry","hindi","gujarati")
    def _compute_result(self):
        for rec in self:
            rec.result = (rec.maths + rec.science + rec.chemistry + rec.hindi + rec.gujarati)/5

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            print("=====vals==", vals.get('heading'), self.env['ir.sequence'].next_by_code('school.student'))
            if vals.get('heading', 'New') == 'New':
                vals['heading'] = self.env['ir.sequence'].next_by_code('average.grade') or '/'
        return super().create(vals_list)