from odoo import api, fields, models
from odoo.exceptions import ValidationError


class Team(models.Model):
    _name = "esports.team"

    id = fields.Integer()
    name = fields.Text()
    foundation = fields.Date()
    coach = fields.Text()

    player_id = fields.Many2many('esports.player', string="Player")

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
