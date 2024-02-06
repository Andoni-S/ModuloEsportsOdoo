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
    'author': "Andoni, ANder and Jago",
    'depends':['project'],
    'license': 'LGPL-3',
    'application': 'true',
    'installable': 'true'
}