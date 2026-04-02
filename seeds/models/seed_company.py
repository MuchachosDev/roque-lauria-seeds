from odoo import fields, models,api
from odoo.exceptions import ValidationError

class SeedCompany(models.Model):
    _name = "seed.company"
    _description = "Companies who send the seeds"

    name = fields.Char(string="Nombre", required=True)
    arrival_order_ids = fields.One2many(
        string="Ordenes de entrada",
        comodel_name="seed.arrival.order",
        inverse_name="laboratory_id"
    )
    @api.constrains('name')
    def _check_name_unique(self):
        for record in self:
            if self.search_count([('name', '=', record.name), ('id', '!=', record.id)]) > 0:
                raise ValidationError('Este campo debe ser único.')