from odoo import fields, models


class ProjectBase(models.Model):
    _name = "project.base"
    _description = "Project Base"

    name = fields.Char(required=True)
