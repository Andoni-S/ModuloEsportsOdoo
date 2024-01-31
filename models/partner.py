# -*- coding: utf-8 -*-
from odoo import fields, models

class Partner(models.Model):
    _inherit = 'res.users'

    games_ids = fields.Many2many('esports.game',string="Games")