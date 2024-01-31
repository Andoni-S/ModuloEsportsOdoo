from datetime import datetime

from odoo import api, fields, models
from odoo.exceptions import ValidationError


class Team(models.Model):
    _name = "esports.team"

    name = fields.Text()
    foundation = fields.Date()
    coach = fields.Text()

    player_id = fields.Many2many('esports.player', string="Player")
    event_id = fields.Many2many('esports.event', string="Event")
    "teamEvent_id = fields.One2many('esports.teamEvent', 'event_id', string='TeamEvent')"

    @api.constrains('name')
    def _checkName(self):
        for record in self:
            if len(record.name) > 20:
                raise ValidationError("Your field is too long: %s" % record.name)
    @api.constrains('foundation')
    def _checkFoundation(self):
        for team in self:
            if team.foundation > fields.Date.today():
                raise ValidationError("The date cannot be a future one.")

    @api.constrains('coach')
    def _checkCoach(self):
        for record in self:
            if len(record.coach) > 20:
                raise ValidationError("Your field is too long: %s" % record.coach)
            if any(char.isdigit() for char in record.coach):
                raise ValidationError("Coach should not contain numbers.")

    @api.onchange('foundation')
    def _onchange_foundation(self):
        if self.foundation:
            current_date = fields.Date.from_string(datetime.now())
            foundation = fields.Date.from_string(self.foundation)
            if foundation > current_date:
                return {
                    'warning': {
                        'title': "Wrong date",
                        'message': "You need to select a past date.",
                    }
                }
        else:
            self.releaseDate = ""