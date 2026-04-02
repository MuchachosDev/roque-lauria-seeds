from odoo import fields, models


class SeedCompany(models.Model):
    _name = "seed.company"
    _description = "Companies who send the seeds"

    name = fields.Char(string="Nombre")
    arrival_order_ids = fields.One2many(
        string="Ordenes de entrada",
        comodel_name="seed.arrival.order",
        inverse_name="laboratory_id"
    )
