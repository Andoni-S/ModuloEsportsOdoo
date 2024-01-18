from odoo import api, fields, models
from odoo import fields, models

class Event(models.Model):
    _name = "esports.event"
    _description = 'Description of your Esports event model'

    name = fields.Char("Name", required=True)
    location = fields.Char("Location")
    ong = fields.Char("NGO")
    date = fields.Datetime("Date")
    prize = fields.Float("Prize")
    donation = fields.Float("Donation")
    """
    prize = fields.Float("Prize", compute='_compute_total_amount', store=True)
    donation_percentage = fields.Float("Donation Percentage", default=0.0,
                                       help="Percentage of the prize to be donated to the NGO")
    donation = fields.Float("Donation", compute='_compute_donation', store=True)
    """
    participant_num = fields.Integer("Participant Number", compute='_compute_participant_num', store=True)
    game_id = fields.Many2one("esports.game", string="Game", required=True)
    organizer_id = fields.Many2one("esports.organizer", string="Organizer", required=True)
    player_ids = fields.Many2many("esports.player", string="Players")
    """"  
    @api.depends('prize', 'donation_percentage')
    def _compute_total_amount(self):
        for event in self:
            event.prize = event.prize or 0.0
            event.total_amount = event.prize

    @api.depends('prize', 'donation_percentage')
    def _compute_donation(self):
        for event in self:
            event.donation = (event.prize * event.donation_percentage) / 100

    @api.depends('player_ids')
    def _compute_participant_num(self):
        for event in self:
            event.participant_num = len(event.player_ids)
    """
    _sql_constraints = [
        ('unique_event_organizer_game', 'unique(organizer_id, game_id, date)', 'An event with the same organizer, game, and date already exists!'),
    ]
