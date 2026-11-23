from odoo import  models, fields

class KriozaCategory(models.Model):
    _name = 'krioza.category'
    _description = 'Krioza Training Category'

    name = fields.Char(string='Category Name', required=True)
    course_ids = fields.One2many('krioza.course', 'category_id', string='Courses')