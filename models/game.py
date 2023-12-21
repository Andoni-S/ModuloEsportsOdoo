from odoo import api, fields, models

class Game(models.Model):
    _name = 'esports.game'
    _description = 'Description of your Esports Game model'

    name = fields.Char()
    genre = fields.Char()
    platform = fields.Char()
    pvp_type = fields.Selection([('1v1', '1 V 1'), ('3v3', '3 V 3'), ('5v5', '5 V 5')],
                                string='PVP Type')
    releaseDate = fields.Date()
