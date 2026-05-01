from odoo import fields, models, api
from odoo.exceptions import ValidationError


class SeedHibrid(models.Model):
    _name = "seed.hibrid"
    _description = "Hibrid Seeds"
    _rec_name = "hibrid_code"

    hibrid_code = fields.Char(
        string="Código",
        tracking=True,
        required=True
    )
    name = fields.Char(string="Nombre", tracking=True)
    laboratory_id = fields.Many2one(
        string="Empresa",
        comodel_name="seed.company",
        required=True
    )
    vegetable_id = fields.Many2one(
        string="Hortaliza",
        comodel_name="seed.vegetable",
        required=True
    )
    arrival_order_ids = fields.One2many(
        comodel_name="seed.arrival.order",
        inverse_name="hibrid_id"
    )
    deperture_order_item_ids = fields.One2many(
        comodel_name="seed.deperture.order.item",
        inverse_name="hibrid_id"
    )
    result_order_item_ids = fields.One2many(
        comodel_name="seed.result.order.item",
        inverse_name="hibrid_id",
    )
    stock_id = fields.One2many(
        string="Stock",
        comodel_name="seed.stock",
        inverse_name="hibrid_id"
    )

    @api.constrains('hibrid_code')
    def _check_name_unique(self):
        for record in self:
            if self.search_count([('hibrid_code', '=', record.hibrid_code), ('id', '!=', record.id)]) > 0:
                raise ValidationError('Este campo debe ser único.')
