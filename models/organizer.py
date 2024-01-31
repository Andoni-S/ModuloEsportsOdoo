from odoo import fields, models, api

class Organizer(models.Model):
    _name = "esports.organizer"
    _description = 'Description of your Esports organizer model'
    _inherit = 'esports.user'

    company = fields.Char("Company")
    web = fields.Char("Web")
    events = fields.One2many("esports.event","organizer_id",string = "Events")
