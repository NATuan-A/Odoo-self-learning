{
    'name': 'Custom POS',
    'version': '1.0',
    'category': 'Point of Sale',
    'summary': 'Customizations for POS',
    'description': """Customizations for POS""",
    'depends': ['point_of_sale'],
    'data': [
        'views/res_config_settings_views.xml',
    ],
    'assets': {
        'point_of_sale.assets': [
            'pos_customer_required/static/src/js/pos_custom_actionpad.js',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
}
