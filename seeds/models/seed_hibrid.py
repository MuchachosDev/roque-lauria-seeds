from odoo import fields, models


class SeedHibrid(models.Model):
    _name = "seed.hibrid"
    _description = "Hibrid Seeds"
    _inherit = ["mail.thread"]
    _rec_name = "hibrid_code"

    hibrid_code = fields.Char(string="Código del hibrido", tracking=True)
    name = fields.Char(string="Nombre", tracking=True)
    laboratory_id = fields.Many2one(string="Empresa", comodel_name="seed.company")
    vegetable_id = fields.Many2one(string="Hortaliza", comodel_name="seed.vegetable")
    arrival_order_ids = fields.One2many(
        comodel_name="seed.arrival.order", inverse_name="hibrid_id"
    )
    deperture_order_item_ids = fields.One2many(
        comodel_name="seed.deperture.order.item", inverse_name="hibrid_id"
    )
    result_order_item_ids = fields.One2many(
        comodel_name="seed.result.order.item",
        inverse_name="hibrid_id",
    )
