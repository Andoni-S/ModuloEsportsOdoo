from odoo import api, fields, models
from odoo.exceptions import ValidationError
from datetime import datetime

class Game(models.Model):
    _name = 'esports.game'
    _description = 'Description of your Esports Game model'

    name = fields.Char()
    genre = fields.Char()
    platform = fields.Char()
    pvp_type = fields.Selection([('1v1', '1 V 1'), ('3v3', '3 V 3'), ('5v5', '5 V 5')], string='PVP Type')
    releaseDate = fields.Date()
    admin_id = fields.Many2one('esports.admin', string="Admin", required=True)
    @api.constrains('name')
    def _checkName(self):
        for record in self:
            if len(record.name) > 20:
                raise ValidationError("Your field is too long: %s" % record.name)
    @api.constrains('genre')
    def _checkGenre(self):
        for record in self:
            if len(record.genre) > 20:
                raise ValidationError("Your field is too long: %s" % record.genre)
            if any(char.isdigit() for char in record.genre):
                raise ValidationError("Genre should not contain numbers.")
    @api.constrains('platform')
    def _checkPlatform(self):
        for record in self:
            if len(record.platform) > 20:
                raise ValidationError("Your field is too long: %s" % record.platform)

    @api.onchange('releaseDate')
    def _onchange_release_date(self):
        if self.releaseDate:
            current_date = fields.Date.from_string(datetime.now())
            release_date = fields.Date.from_string(self.releaseDate)
            if release_date > current_date:
                return {
                    'warning': {
                        'title': "Wrong release date",
                        'message': "Careful, your release date is after today",
                    }
                }
        else:
            self.releaseDate = ""

    @api.model
    def create(self, values):
        current_date = fields.Date.from_string(datetime.now())
        release_date = fields.Date.from_string(values.get('releaseDate'))
        if release_date > current_date:
            values['releaseDate'] = current_date
            print("release date is after today, today´s date assigned")

        res = super(Game, self).create(values)
        # here you can do accordingly
        return res

