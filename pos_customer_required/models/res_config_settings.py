from odoo import models, fields

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    pos_customer_required = fields.Boolean(
        related='pos_config_id.customer_required',
        readonly=False,
        string="Customer Required (PoS)"
    )
