from odoo import fields, models


class SeedCompany(models.Model):
    _name = "seed.company"
    _description = "Companies who send the seeds"

    name = fields.Char(string="Nombre", required=True)
    arrival_order_ids = fields.One2many(
        string="Ordenes de entrada",
        comodel_name="seed.arrival.order",
        inverse_name="laboratory_id"
    )
    _sql_constraints = [
    ('name_unique', 'unique(name)', 'Este campo debe ser único.')
]
