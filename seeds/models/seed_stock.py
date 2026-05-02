from odoo import api, fields, models
from odoo.exceptions import ValidationError

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

    @api.constrains("amount")
    def _check_positive_amount(self):
        for rec in self:
            if rec.amount < 0:
                raise ValidationError("El stock no puede ser negativo")
