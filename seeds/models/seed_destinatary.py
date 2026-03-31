from odoo import fields, models


class SeedDestinatary(models.Model):
    _name = "seed.destinatary"
    _description = "Destinatiries"

    name = fields.Char(string="Nombre completo")
    deperture_order_ids = fields.One2many(
        string="Ordenes de salida",
        comodel_name="seed.deperture.order",
        inverse_name="destinatary_name"
    )
