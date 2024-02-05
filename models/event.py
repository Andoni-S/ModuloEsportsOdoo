from odoo import api, fields, models

from odoo import fields, models

class Event(models.Model):
    _name = "esports.event"
    _description = 'Description of your Esports event model'

    name = fields.Char("Name", required=True)
    location = fields.Char("Location")
    imagen = fields.Binary(string="Image", attachment=True)
    ong = fields.Char("NGO")
    date = fields.Datetime("Date")
    prize = fields.Float("Prize")
    donation = fields.Float("Donation")
    participant_num = fields.Integer("Participant Number")
    game_id = fields.Many2one('esports.game', string="Game", required=True)
    organizer_id = fields.Many2one('esports.organizer', string="Organizer", required=True)
    player_id = fields.Many2many('esports.player', string="Players")
    team_id = fields.Many2many('esports.team', string="Team")

    _sql_constraints = [
        ('unique_event_organizer_game', 'unique(organizer_id, game_id, date)', 'An event with the same organizer, game, and date already exists!'),
    ]

