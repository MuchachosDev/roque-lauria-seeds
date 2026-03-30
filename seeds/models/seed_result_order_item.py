from odoo import api, fields, models


class SeedResultOrderItem(models.Model):
    _name = "seed.result.order.item"
    _description = "Result order items"

    land_code = fields.Char(string="Código de campo")
    evaluation_date = fields.Date(string="Fecha de evaluación")
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

    @api.onchange("hibrid_id")
    def _onchange_hibrid_id_load_template(self):
        for rec in self:
            rec.experiment_result = False

            if not rec.hibrid_id or not rec.hibrid_id.vegetable_id:
                continue

            template = self.env["seed.experiment.result.template"].search(
                [("vegetable_id", "=", rec.hibrid_id.vegetable_id.id)],
                limit=1,
            )

            rec.experiment_result = template.template if template else False