from odoo import api, fields, models

class Player(models.Model):
    _name = 'esports.player'
    _description = 'Description of your Esports player model'
    _inherit = 'esports.user'
