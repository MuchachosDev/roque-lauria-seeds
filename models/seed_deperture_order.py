from odoo import api, fields, models


class SeedDepertureOrder(models.Model):
    _name = "seed.deperture.order"
    _description = "Deperture orders"

    order_number = fields.Char("Orden de salida N°", compute="_compute_order_number")
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
        reverse_name="deperture_order_id",
    )

    @api.depends("id")
    def _compute_order_number(self):
        for record in self:
            if record.id:
                record.order_number = str(record.id).zfill(10)
