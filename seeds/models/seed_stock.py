from odoo import fields, models

class SeedStock(models.Model):
    _name = "seed.stock"
    _description = "Stock of the seeds"

    _sql_constraints = [
        (
         'unique_hibrid_package',
         'unique(hibrid_id, package_type)',
         'Ya existe un registro de stock para este híbrido y presentación.'
        )
    ]

    hibrid_id = fields.Many2one(
        string="Híbrido",
        comodel_name="seed.hibrid"
    )
    package_type = fields.Selection(
        string="Tipo de presentación",
        selection=[("seed", "Semilla"), ("letter_envelope", "Sobre")],
        default="seed",
    )
    amount = fields.Integer(string="Cantidad")
