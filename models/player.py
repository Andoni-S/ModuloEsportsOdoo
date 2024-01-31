from odoo import fields, models

class Player(models.Model):
    _name = "esports.player"
    _inherit = 'esports.user'

    level = fields.Integer()

    team_id = fields.Many2many('esports.team',string="Team")