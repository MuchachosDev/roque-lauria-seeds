from odoo import fields, models


class SeedCompany(models.Model):
    _name = "seed.company"
    _description = "Companies who send the seeds"

    name = fields.Char(string="Nombre")
