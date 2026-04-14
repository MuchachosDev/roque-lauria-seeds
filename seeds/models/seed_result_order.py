from odoo import api, fields, models


class SeedResultOrder(models.Model):
    _name = "seed.result.order"
    _description = "Result orders"
    _rec_name = "order_number"

    order_number = fields.Char(
        string="Orden de resultado",
        default="Nueva orden de resultados",
        readonly=True,
        copy=False,
    )
    start_date = fields.Date(string="Fecha de inicio")
    end_date = fields.Date(string="Fecha de finalización")
    seed_date = fields.Date(string="Fecha de siembra")
    replant_date = fields.Date(string="Fecha de transplante")
    test_fiability = fields.Char(string="Confiabilidad del ensayo")
    season = fields.Char(string="Temporada")
    farmer = fields.Many2one(
        string="Agricultor",
        comodel_name="seed.destinatary",
        required=True
    )
    distributor = fields.Char(string="Distribuidor")
    lines_amount = fields.Integer(string="Cantidad de líneas plantadas")
    substratum = fields.Char(string="Sustrato")
    lat_coord = fields.Float(string="Latitud")
    lon_coord = fields.Float(string="Longitud")
    harvest_method = fields.Char(string="Método de cosecha")
    item_ids = fields.One2many(
        comodel_name="seed.result.order.item", inverse_name="result_order_id"
    )

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if (
                vals.get("order_number", "Nueva orden de resultados")
                == "Nueva orden de resultados"
            ):
                vals["order_number"] = (
                    self.env["ir.sequence"].next_by_code("seed.result.order")
                    or "Nueva orden de resultados"
                )
        return super().create(vals_list)
