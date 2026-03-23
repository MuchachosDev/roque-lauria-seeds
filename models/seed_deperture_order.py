from email.policy import default

from odoo import api, fields, models


class SeedDepertureOrder(models.Model):
    _name = "seed.deperture.order"
    _description = "Deperture orders"

    order_number = fields.Char("Orden de salida N°", readonly=True, copy=False, default="Nuevo")
    deperture_date = fields.Date(string="Fecha de envío")
    arrival_date = fields.Date(string="Fecha de reepción")
    # Ver esto porque podría ser una relación con el modelo "res.partner"
    destinatary_name = fields.Char(string="Destinatario")
    # Se podría crear otra tabla para este campo o sacarlo de la relación
    # que tendría que estar en destinatary_name
    destinatary_city = fields.Char(string="Localidad del destinatario")
    batch = fields.Char("Batch")
    observation = fields.Html(string="Observaciones")
    item_ids = fields.One2many(
        string="Contenido de la orden",
        comodel_name="seed.deperture.order.item",
        inverse_name="deperture_order_id",
    )

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get("order_number", "Nuevo") == "Nuevo":
                vals["order_number"] = self.env["ir.sequence"].next_by_code(
                    "seed.deperture.order"
                ) or "Nuevo"
        return super().create(vals_list)
