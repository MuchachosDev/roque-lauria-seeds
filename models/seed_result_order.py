from odoo import fields, models


class SeedResultOrder(models.Model):
    _name = "seed.result.order"
    _description = "Result orders"

    start_date = fields.Date(string="Fecha de inicio")
    end_date = fields.Date(string="Fecha de finalización")
    seed_date = fields.Date(string="Fecha de siembra")
    replant_date = fields.Date(string="Fecha de transplante")
    test_fiability = fields.Char(string="Confiabilidad del ensayo")
    season = fields.Char(string="Temporada")
    farmer = fields.Char(string="Nombre del agricultor")
    distributor = fields.Char(string="Distribuidor")
    lines_amount = fields.Integer(string="Cantidad de líneas plantadas")
    substratum = fields.Char(string="Sustrato")
    lat_coord = fields.Float(string="Latitud")
    lon_coord = fields.Float(string="Longitud")
    harvest_method = fields.Char(string="Método de cosecha")
    result_order_item_ids = fields.One2many(
        comodel_name="seed.result.order.item", inverse_name="result_order_id"
    )
