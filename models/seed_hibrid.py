from odoo import fields, models


class SeedHibrid(models.Model):
    _name = "seed.hibrid"
    _description = "Hibrid Seeds"
    _inherit = ["mail.thead"]

    hibrid_code = fields.Char(string="Código del hibrido")
    name = fields.Char(string="Nombre", traked=True)
    company_id = fields.Many2one(string="Empresa", comodel_name="seed.company")
    vegetable_id = fields.Many2one(string="Hortaliza", comodel_name="seed.vegetable")
    result_order_id = fields.One2many(
        string="Orden de resultados",
        comodel_name="seed.result.order",
        reverse_name="hibrid_id",
    )
