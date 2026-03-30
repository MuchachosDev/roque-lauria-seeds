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
            if (
                vals.get("order_number", "Nueva orden de salida")
                == "Nueva orden de salida"
            ):
                vals["order_number"] = (
                    self.env["ir.sequence"].next_by_code("seed.deperture.order")
                    or "Nueva orden de salida"
                )
        return super().create(vals_list)
