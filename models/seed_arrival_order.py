from email.policy import default

from odoo import api, fields, models


class SeedArrivalOrder(models.Model):
    _name = "seed.arrival.order"
    _description = "Arrival orders"

    order_number = fields.Char(
        string="Orden de entrada N°", readonly=True, copy=False, default="Nuevo"
    )
    arrival_date = fields.Date(string="Fecha de ingreso", default=fields.Date.today)
    invoice_number = fields.Char(string="Número de factura")
    hibrid_id = fields.Many2one(string="Híbrido")
    hibrid_name = fields.Char(string="Nombre del hibrido", related="hibrid_id.name")
    company_id = fields.Many2one(
        string="Empresa proveedora",
        comodel_name="seed.company",
        related="hibrid_id.company_id",
        store=True,
    )
    vegetable_id = fields.Many2one(
        string="Hortaliza",
        comodel_name="seed.vegetable",
        related="hibrid_id.vegetable_id",
    )
    amount = fields.Integer(string="Cantidad")
    observation = fields.Html()
    # Detalle tecnico
    fruit_shape = fields.Char(string="Forma del fruto o cabeza")
    thorn = fields.Boolean(string="Espinas")
    fruit_colour = fields.Char(string="Color de la fruta o cabeza")
    avg_weight = fields.Float(string="Peso promedio del fruto o cabeza", digits=(6, 2))
    core_colour = fields.Char(string="Color de la pulpa")
    peel_type = fields.Char(string="Tipo de cáscara")
    peel_width = fields.Char(string="Grosor de la cáscara")
    production = fields.Char(string="Producción")
    transport_behaviour = fields.Char(string="Comportamiento durante el traslado")
    brix_degrees = fields.Float(string="Grados Brixs", digits=(4, 2))
    post_harvesting = fields.Char(string="Post cocecha")
    uniformity = fields.Char(string="Uniformidad")
    neck_quality = fields.Char(string="Calidad del cuello")
    cycle = fields.Char(string="Ciclo")
    leaves_color = fields.Char(string="Color de follaje")
    leave_type = fields.Char(string="Tipo de hoja")
    vegetative_development = fields.Char(string="Desarrollo vegetativo")
    leaves_coverage = fields.Char(string="Cobertura de hojas")
    plant_quality = fields.Char(string="Calidad de la planta")
    knots = fields.Char(string="Entrenudos")
    sanity = fields.Char(string="Sanidad")
    resistance = fields.Char(string="Resistencia y/o tolerancia")

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get("order_number", "Nuevo") == "Nuevo":
                vals["order_number"] = self.env["ir.sequence"].next_by_code(
                    "seed.arrival.order"
                ) or "Nuevo"
        return super().create(vals_list)
