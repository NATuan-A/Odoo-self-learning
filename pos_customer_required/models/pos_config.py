# /path/to/odoo/addons/custom_pos/models/pos_config.py

from odoo import models, fields

class PosConfig(models.Model):
    _inherit = 'pos.config'

    customer_required = fields.Boolean(string="Customer Required")
