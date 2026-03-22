from odoo import fields, models


class SeedVegetable(models.Model):
    _name = "seed.vegetable"
    _description = "Vegetables"

    name = fields.Char(string="Nombre")
    experiment_result_template_id = fields.One2many(
        string="Plantilla de resultados",
        comodel_name="seed.experiment.result.template",
        reverse_name="vegetable_id",
    )
