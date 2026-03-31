from odoo import fields, models


class SeedLocation(models.Model):
    _name = "seed.location"
    _description = "Locations"

    name = fields.Char(string="Nombre de la localidad")
    company_id = fields.Many2one(
        string='Compañía',
        comodel_name='res.company',
        default=lambda self: self.env.company
    )
    state_id = fields.Many2one(
        string="Provincia",
        comodel_name="res.country.state",
        domain="[('country_id', '=', company_id.country_id)]"
    )
    deperture_order_ids = fields.One2many(
        string="Ordenes de salida",
        comodel_name="seed.deperture.order",
        inverse_name="destinatary_city"
    )
