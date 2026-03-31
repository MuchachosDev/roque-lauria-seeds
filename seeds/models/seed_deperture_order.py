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
    deperture_date = fields.Date(string="Fecha de envío")
    arrival_date = fields.Date(string="Fecha de recepción")
    destinatary_name = fields.Many2one(
        string="Destinatario",
        comodel_name="seed.destinatary"
    )
    destinatary_city = fields.Many2one(
        string="Localidad de destino",
        comodel_name="seed.location"
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
