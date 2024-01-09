from odoo import fields, models

class Event(models.Model):
    _name = "esports.event"

    name = fields.Char("Name")
    location = fields.Char("Location")
    ong = fields.Char("NGO")
    date = fields.Datetime("Date")
    prize = fields.Float("Prize")
    donation = fields.Float("Donation")
    participant_num = fields.Integer("Participant Number")
    #game_id = fields.Many2one("esporthub.game", string="Game")
    #organizer_id = fields.Many2one("esporthub.organizer", string="Organizer")