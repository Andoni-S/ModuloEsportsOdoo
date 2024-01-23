from odoo import fields, models

class TeamEvent(models.Model):
    _name = "esports.teamevent"

    result = fields.String()

    team_id = fields.Many2one('team.Model', string="Team")
    event_id = fields.Many2one('event.Model', string="Event")