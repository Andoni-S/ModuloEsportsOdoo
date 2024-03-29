# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': "eSportsHub",
    'category': "App",
    'summary': """eSports eventos managing app""",
    'version': "1.0",
    'data': [
        'security/eSports_security.xml',
        'security/ir.model.access.csv',
        'views/templates.xml',
        'views/eSports.xml',
        'views/game.xml',
        'views/partner.xml',
        'views/team.xml',
        'views/event.xml',
        'report/reports.xml'],
    'description': """eSportsHub is an application to manage events for online Sports""",
    'author': "Andoni",
    'depends':['project'],
    'website': "web?debug=1#action=85&model=esports.game&view_type=kanban&cids=1&menu_id=70",
    'license': 'LGPL-3',
    'application': 'true',
    'installable': 'true'
}