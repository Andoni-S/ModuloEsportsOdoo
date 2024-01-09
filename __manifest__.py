# -*- coding: utf-8 -*-
{
    'name': "eSportsHub",
    'category': "App",
    'summary': """eSports events managing app""",
    'version': '1.0.0',
    'description': """
        App to manage eSports events from different games.
    """,
    'author': "Group 1",
    'website': "https://www.tartanga.eus",


    # any module necessary for this one to work correctly
    'depends': [],
    #'depends': ['mail'],

    # always loaded
    'data': [
        'security/eSports_security.xml',
        'security/ir.model.access.csv',
        'views/templates.xml',
        'views/eSports.xml',
    ]
}
