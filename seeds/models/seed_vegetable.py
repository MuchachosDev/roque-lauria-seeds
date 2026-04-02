from odoo import fields, models


class SeedVegetable(models.Model):
    _name = "seed.vegetable"
    _description = "Vegetables"

    name = fields.Char(string="Nombre", required=True)

    _sql_constraints = [
    ('name_unique', 'unique(name)', 'Este campo debe ser único.')
]
