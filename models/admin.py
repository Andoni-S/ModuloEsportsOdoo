from odoo import models, api, fields, exceptions
from odoo.exceptions import ValidationError, UserError

class Admin(models.Model):
    _name = 'esports.admin'
    _description = 'User for the Esports app that adds the games'
    _inherit = 'esports.user'

    entryYear = fields.Date()
