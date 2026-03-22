from odoo import fields, models


class SeedExperimentResultTemplate(models.Model):
    _name = "seed.experiment.result.template"
    _description = (
        "Templates wich show specifica fields acording to the vegetable evaluated"
    )

    name = fields.Char(string="Nombre de la plantilla")
    template = fields.Html(string="Plantilla")
    vegetable_id = fields.Many2one(string="Hortaliza", comodel_name="seed.vegetable")
