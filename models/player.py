from odoo import fields, models

class Player(models.Model):
    _name = "esports.player"

    id = fields.Integer()
    level = fields.Integer()

    team_id = fields.Many2many('Team.Model',string="Team")