from odoo import fields, models,api
from datetime import date


class books(models.Model):
    _name = "books.books"
    _description = "student details"


    name = fields.Char(string="Tittle")
    author = fields.Many2one('res.partner',string="Author")
    public_date = fields.Date(string="Publication Date")
    age = fields.Char(string="Age",compute='_compute_age')

    def _compute_age(self):
        for age in self:
            today = date.today()
            if age.public_date:
                age.age = today.year - age.public_date.year
            else:
                age.age = 0

    @api.onchange('author')
    def onchange_author(self):
        if self.author:
            if self.author.create_date:
                self.public_date = self.author.create_date
