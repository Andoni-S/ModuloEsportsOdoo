from odoo import fields,models,api

class Organizer(models.Model):
    _name = "esporthub.organizer"
    
    company = fields.Char("Company")
    web = fields.Char("Web")
    #events = fields.One2Many("esporthub.event","organizer_id",string = "Events")