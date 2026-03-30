from odoo import fields, models


class SeedVegetable(models.Model):
    _name = "seed.vegetable"
    _description = "Vegetables"

    name = fields.Char(string="Nombre")
