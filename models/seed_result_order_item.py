from odoo import api, fields, models


class SeedResultOrderItem(models.Model):
    _name = "seed.result.order.item"
    _description = "Result order items"

    land_code = fields.Char(string="Código de campo")
    evaluation_date = fields.Date(string="Fecha de evalución")
    experiment_result = fields.Html()
    hibrid_id = fields.Many2one(string="Variedad", comodel_name="seed.hibrid")
    vegetable_name = fields.Char(
        string="Hortaliza", related="hibrid_id.vegetable_id.name"
    )
    result_order_id = fields.Many2one(comodel_name="seed.result.order")
    photo = fields.Many2many(
        string="Fotos y Videos",
        comodel_name="ir.attachment",
        relation="result_order_item_attachment_rel",
        column1="result_order_item_id",
        column2="attachment_id",
    )

    @api.depends("hibrid_id")
    def _lead_result_template(self):
        vegetable = self.hibrid_id.vegetable_id
        if self.hibrid_id and vegetable:
            self.experiment_result = vegetable.experiment_result_template_id.template
