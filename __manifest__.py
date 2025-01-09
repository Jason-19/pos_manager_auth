# -*- coding: utf-8 -*-
{
    'name':'Manager Auth Pos',
    'summary': 'Restringir reembolso de POS con contraseña',
    'version': '17.0.1.0.1',
    'category': 'Point of Sale',
    'author': '',
    'depends': ['point_of_sale','hr'],
    'data': [
        'views/pos_config_views.xml',
        'views/res_config_settings_views.xml',
        'views/hr_employee_views.xml',
        'security/security.xml',
        'security/ir.model.access.csv'
    ],
    'assets': {
        'point_of_sale._assets_pos': [
            'pos_manager_auth/static/src/js/refund/refund_auth.js',
            'pos_manager_auth/static/src/js/disconunt/payment_scree.js',
            'pos_manager_auth/static/src/js/disconunt/pos_store.js',
            'pos_manager_auth/static/src/xml/navbar_logo.xml',
            "pos_manager_auth/static/src/xml/receipt_logo.xml"
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
    "sequence":'1'
}