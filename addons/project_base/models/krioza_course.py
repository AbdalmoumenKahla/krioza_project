
from odoo import models, fields


class KriozaCourse(models.Model):
    _name = 'krioza.course'
    _description = 'Krioza Training Course'
    _order = 'name'

    name = fields.Char(
        string='Course Name',
        required=True
    )

    code = fields.Char(
        string='Course Code',
        help='Short code like ODOO',
        required=True
    )

    description = fields.Text(
        string='Course Description'
    )

    duration = fields.Integer(
        string='Duration (in hours)',
        required=True,
        default=20
    )
    level = fields.Selection(
        [('beginner', 'Beginner'),
         ('intermediate', 'Intermediate'),
         ('advanced', 'Advanced')],
        string='Course Level',
        required=True,
        default='beginner'
    )
    start_date = fields.Date(
        string='Start Date',
        required=True
    )
    end_date = fields.Date(
        string='End Date',
        required=True
    )
    syllabus = fields.Html(
        string='Syllabus',
        sanitize=True
    )
    online = fields.Boolean(
        string='Online Course',
        default=False
    )