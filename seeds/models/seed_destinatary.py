from odoo import api, fields, models


class SeedDestinatary(models.Model):
    _name = "seed.destinatary"
    _description = "Destinataries"
    _rec_name = "first_name"

    def _get_default_country(self):
        # return self.env.user.partner_id.country_id
        return self.env.ref("base.ar")

    complete_name = fields.Char(string="Nombre completo", compute="_compute_complete_name")
    first_name = fields.Char(string="Nombre", required=True)
    last_name = fields.Char(string="Apellido", required=True)

    country_id = fields.Many2one(
        string="País",
        comodel_name="res.country",
        default=_get_default_country,
    )
    state_id = fields.Many2one(
        string="Provincia",
        comodel_name="res.country.state",
        domain="[('country_id', '=', country_id)]",required=True
    )
    city = fields.Char(string="Nombre de la localidad",required=True)
    location_name = fields.Char(
        string="Localidad de destino",
        compute="_compute_location_name"
    )

    deperture_order_ids = fields.One2many(
        string="Ordenes de salida",
        comodel_name="seed.deperture.order",
        inverse_name="destinatary_id",
    )

    @api.depends("first_name", "last_name")
    def _compute_complete_name(self):
        for rec in self:
            first_name = rec.first_name or ""
            last_name = rec.last_name or ""
            if first_name and last_name:
                rec.complete_name = f"{last_name} {first_name}"
            else:
                rec.complete_name = "Nuevo destinatario"

    @api.depends("country_id", "state_id", "city")
    def _compute_location_name(self):
        for rec in self:
            city = rec.city or ""
            state = rec.state_id.name or ""
            country = rec.country_id.name or ""

            res = ", ".join(filter(None, [city, state, country]))
            rec.location_name = res or "Sin ubicación"
