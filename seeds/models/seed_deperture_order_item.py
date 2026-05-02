from odoo import api, fields, models
from odoo.exceptions import ValidationError


class SeedDepertureOrderItem(models.Model):
    _name = "seed.deperture.order.item"
    _description = "Deperture order items"

    vegetable = fields.Char(
        string="Hortaliza",
        related="hibrid_id.vegetable_id.name"
    )
    hibrid_code = fields.Char(
        string="Código del híbrido",
        related="hibrid_id.hibrid_code"
    )
    hibrid_name = fields.Char(
        string="Nombre del híbrido",
        related="hibrid_id.name"
    )
    amount = fields.Integer(
        string="Cantidad",
        required=True
    )
    package_type = fields.Selection(
        string="Tipo de presentación",
        selection=[("seed", "Semilla"), ("letter_envelope", "Sobre")],
        default="seed",
        required=True
    )
    hibrid_id = fields.Many2one(
        string="Híbrido",
        comodel_name="seed.hibrid",
        required=True
    )
    deperture_order_id = fields.Many2one(
        string="Orden de salida",
        comodel_name="seed.deperture.order"
    )

    @api.constrains('amount', 'hibrid_id', 'package_type')
    def _check_stock_limit(self):
        for rec in self:
            stock = self.env['seed.stock'].search([
                    ('hibrid_id', '=', rec.hibrid_id.id),
                    ('package_type', '=', rec.package_type)
                ],
                limit=1
            )

            if not stock or stock.amount < 0:
                available = (stock.amount + rec.amount) if stock else 0
                package_type = dict(self._fields['package_type'].selection).get(rec.package_type)
                raise ValidationError(
                    f"Stock insuficiente para {rec.hibrid_name} ({package_type}). Cantidad disponible: {available}"
                )

    @api.model_create_multi
    def create(self, vals_list):
        recs = super().create(vals_list)
        for rec in recs:
            stock = self.env['seed.stock'].search([
                    ('hibrid_id', '=', rec.hibrid_id.id),
                    ('package_type', '=', rec.package_type)
                ],
                limit=1
            )

            if stock:
                stock.amount -= rec.amount

        return recs

    def write(self, vals):
        if 'amount' in vals:
            for rec in self:
                diff = vals['amount'] - rec.amount
                stock = self.env['seed.stock'].search([
                        ('hibrid_id', '=', rec.hibrid_id.id),
                        ('package_type', '=', rec.package_type)
                    ],
                    limit=1
                )
                if stock:
                    stock.amount -= diff

        return super().write(vals)

    def unlink(self):
        for rec in self:
            stock = self.env['seed.stock'].search([
                ('hibrid_id', '=', rec.hibrid_id.id),
                ('package_type', '=', rec.package_type)
            ], limit=1)
            if stock:
                stock.amount += rec.amount
        return super().unlink()
