from odoo import models, api, fields, exceptions
from odoo.exceptions import ValidationError, UserError

class User(models.Model):
    _name = 'esports.user'
    _description = 'Superclass User model for the admin, organizer and player classes'

    username = fields.Char()
    password = fields.Char()
    email = fields.Char()
    name = fields.Char()
    surnames = fields.Char()
    age = fields.Integer()
