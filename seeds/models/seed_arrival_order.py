from odoo import api, fields, models


class SeedArrivalOrder(models.Model):
    _name = "seed.arrival.order"
    _description = "Arrival orders"
    _rec_name = "order_number"

    order_number = fields.Char(
        string="Orden de entrada",
        default="Nueva orden de entrada",
        readonly=True,
        copy=False,
    )
    arrival_date = fields.Date(
        string="Fecha de ingreso",
        default=fields.Date.today,
        required=True
    )
    invoice_number = fields.Char(string="Número de factura")
    hibrid_id = fields.Many2one(
        string="Híbrido",
        comodel_name="seed.hibrid",
        required=True
    )
    hibrid_name = fields.Char(
        string="Nombre del hibrido",
        related="hibrid_id.name"
    )
    package_type = fields.Selection(
        string="Tipo de presentación",
        selection=[("seed", "Semilla"), ("letter_envelope", "Sobre")],
        default="seed",
    )
    laboratory_id = fields.Many2one(
        string="Empresa proveedora",
        comodel_name="seed.company",
        related="hibrid_id.laboratory_id"
    )
    vegetable_id = fields.Many2one(
        string="Hortaliza",
        comodel_name="seed.vegetable",
        related="hibrid_id.vegetable_id"
    )
    amount = fields.Integer(string="Cantidad", required=True)
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
    post_harvesting = fields.Char(string="Post cosecha")
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
            if (
                vals.get("order_number", "Nueva orden de entrada")
                == "Nueva orden de entrada"
            ):
                vals["order_number"] = (
                    self.env["ir.sequence"].next_by_code("seed.arrival.order")
                    or "Nueva orden de entrada"
                )
        return super().create(vals_list)
