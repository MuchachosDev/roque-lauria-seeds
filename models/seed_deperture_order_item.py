from odoo import fields, models


class SeedDepertureOrderItem(models.Model):
    _name = "seed.deperture.order.item"
    _description = "Deperture order item"

    deperture_order_id = fields.Many2one(
        string="Orden de salida", comodel_name="seed.deperture.order"
    )
    hibrid_id = fields.Many2one(string="Híbrido", comodel_name="seed.hibrid")
    vegetable = fields.Char(string="Hortaliza", related="hibrid_id.vegetable_id.name")
    hibrid_code = fields.Char(
        string="Código del híbrido", related="hibrid_id.hibrid_code"
    )
    hibrid_name = fields.Char(string="Nombre del híbrido", related="hibrid_id.name")
    amount = fields.Integer(string="Cantidad")
    package_type = fields.Selection(
        string="Tipo de presentación",
        selection=[("seed", "Semilla"), ("letter_envelope", "Sobre")],
        default="seed",
    )
