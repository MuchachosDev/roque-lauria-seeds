from odoo.exceptions import ValidationError
from odoo import fields, models, api


class SeedVegetable(models.Model):
    _name = "seed.vegetable"
    _description = "Vegetables"

    name = fields.Char(string="Nombre", required=True)

    @api.constrains('name')
    def _check_name_unique(self):
        for record in self:
            if self.search_count([('name', '=', record.name), ('id', '!=', record.id)]) > 0:
                raise ValidationError('Este campo debe ser único.')
