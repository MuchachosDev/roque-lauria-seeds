from odoo import fields, models


class SeedResultOrder(models.Model):
    _name = "seed.result.order"
    _description = "Result orders"

    hibrid_id = fields.Many2one(string="Hibrido", comodel_name="seed.hibrid")
    vegetable_name = fields.Char(
        string="Hortaliza", related="hibrid_id.vegetable_id.name"
    )
    start_date = fields.Date(string="Fecha de inicio")
    end_date = fields.Date(string="Fecha de finalización")
    seed_date = fields.Date(string="Fecha de siembra")
    replant_date = fields.Date(string="Fecha de transplante")
    test_feability = fields.Char(string="Confiabilidad del ensayo")
    season = fields.Char(string="Temporada")
    farmer = fields.Char(string="Nombre del agricultor")
    distributor = fields.Char(string="Distribuidor")
    lines_amount = fields.Integer(string="Cantidad de líneas plantadas")
    substratum = fields.Char(string="Sustrato")
    lat_coord = fields.Float(string="Latitud")
    lon_coord = fields.Float(string="Longitud")
    harvest_method = fields.Char(string="Método de cosecha")
    photo = fields.Many2many(
        string="Fotos",
        comodel_name="ir.attachment",
        relation="result_order_attachment_rel",
        column1="result_order_id",
        column2="attachment_id",
    )
    experiment_result = fields.Html(
        related="hibrid_id.vegetable_id.experiment_result_template_id.template"
    )
