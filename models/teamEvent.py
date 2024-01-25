from odoo import fields, models

class TeamEvent(models.Model):
    _name = "esports.teamevent"

    result = fields.String()

    team_id = fields.Many2one('esports.team','teamEvent_ids', string="Team")
    event_id = fields.Many2one('esports.event','teamEvent_ids', string="Event")