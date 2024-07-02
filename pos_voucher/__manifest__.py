{
    'name': 'Voucher POS',
    'version': '1.0',
    'category': 'Point of Sale',
    'summary': 'Voucher for POS',
    'description': """Voucher for POS""",
    'depends': ['point_of_sale'],
    'data': [
        'security/ir.model.access.csv',
        'security/pos_voucher_security.xml',
        'views/pos_voucher_views.xml'
    ],
    'assets': {
        'point_of_sale.assets': [
            'pos_voucher/static/src/js/pos_voucher_button.js',
            'pos_voucher/static/src/xml/pos_voucher_template.xml',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
}
