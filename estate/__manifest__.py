# -*- coding: utf-8 -*-
{
    'name': "estate",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',
    'data': [
        'security/user_security.xml',
        'security/ir.model.access.csv',
        'views/estate_property_offer_views.xml',
        'views/estate_property_type_views.xml',
        'views/estate_property_tag_views.xml',
        'views/estate_property_views.xml',
        'views/estate_user_views.xml',
        'views/estate_update_price_views.xml',
        'report/estate_reports.xml',
        'report/estate_report_views.xml',
        'views/estate_menus.xml',
    ],
    "demo": [
        "data/estate_demo.xml"
    ],
    # any module necessary for this one to work correctly
    'depends': ['base'],
}
