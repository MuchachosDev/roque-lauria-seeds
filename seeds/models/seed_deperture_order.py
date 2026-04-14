from odoo import api, fields, models


class SeedDepertureOrder(models.Model):
    _name = "seed.deperture.order"
    _description = "Deperture orders"
    _rec_name = "order_number"

    order_number = fields.Char(
        string="Orden de salida",
        default="Nueva orden de salida",
        readonly=True,
        copy=False,
    )
    deperture_date = fields.Date(
        string="Fecha de envío",
        required=True
    )
    arrival_date = fields.Date(
        string="Fecha de recepción",
        required=True
    )
    destinatary_id = fields.Many2one(
        string="Agricultor",
        comodel_name="seed.destinatary",
        required=True
    )
    destinatary_city = fields.Char(
        string="Localidad de destino",
        related="destinatary_id.location_name",
        store=True
    )
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
            if (
                vals.get("order_number", "Nueva orden de salida")
                == "Nueva orden de salida"
            ):
                vals["order_number"] = (
                    self.env["ir.sequence"].next_by_code("seed.deperture.order")
                    or "Nueva orden de salida"
                )
        return super().create(vals_list)
