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
        required=True
    )
    laboratory_id = fields.Many2one(
        string="Empresa proveedora",
        comodel_name="seed.company",
        related="hibrid_id.laboratory_id",
        required=True
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

    def _update_stock(self, hibrid_id, package_type, quantity):
        if not hibrid_id or not package_type:
            return

        stock = self.env['seed.stock'].search([
            ('hibrid_id', '=', hibrid_id),
            ('package_type', '=', package_type)
        ], limit=1)

        if stock:
            stock.amount += quantity

        elif quantity > 0:
            self.env['seed.stock'].create({
                'hibrid_id': hibrid_id,
                'package_type': package_type,
                'amount': quantity
            })

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get("order_number", "Nueva orden de entrada") == "Nueva orden de entrada":
                vals["order_number"] = (
                    self.env["ir.sequence"].next_by_code("seed.arrival.order")
                    or "Nueva orden de entrada"
                )

            hibrid_id = vals.get('hibrid_id')
            package_type = vals.get('package_type')
            amount = vals.get('amount', 0)

            if hibrid_id and package_type:
                stock_record = self.env['seed.stock'].search([
                        ('hibrid_id', '=', hibrid_id),
                        ('package_type', '=', package_type)
                    ],
                    limit=1
                )

                if stock_record:
                    stock_record.amount += amount
                else:
                    self.env['seed.stock'].create({
                            'hibrid_id': hibrid_id,
                            'package_type': package_type,
                            'amount': amount
                        }
                    )

        return super().create(vals_list)

    def write(self, vals):
        for rec in self:
            if 'amount' in vals and 'hibrid_id' not in vals and 'package_type' not in vals:
                diff = vals['amount'] - rec.amount
                self._update_stock(rec.hibrid_id.id, rec.package_type, diff)

            elif 'hibrid_id' in vals or 'package_type' in vals:
                self._update_stock(rec.hibrid_id.id, rec.package_type, -rec.amount)

                new_hibrid = vals.get('hibrid_id', rec.hibrid_id.id)
                new_type = vals.get('package_type', rec.package_type)
                new_amount = vals.get('amount', rec.amount)

                self._update_stock(new_hibrid, new_type, new_amount)

        return super(SeedArrivalOrder, self).write(vals)

    def unlink(self):
        for rec in self:
            self._update_stock(rec.hibrid_id.id, rec.package_type, -rec.amount)

        return super(SeedArrivalOrder, self).unlink()
