from odoo import fields, models


class SeedLocation(models.Model):
    _name = "seed.location"
    _description = "Locations"

    def _get_default_country(self):
        # return self.env.user.partner_id.country_id.id
        return self.env.ref("base.ar")

    name = fields.Char(string="Nombre de la localidad")
    country_id = fields.Many2one(
        string="País",
        comodel_name="res.country",
        default=_get_default_country,
    )
    state_id = fields.Many2one(
        string="Provincia",
        comodel_name="res.country.state",
        domain="[('country_id', '=', country_id)]",
    )
    deperture_order_ids = fields.One2many(
        string="Ordenes de salida",
        comodel_name="seed.deperture.order",
        inverse_name="destinatary_city",
    )
