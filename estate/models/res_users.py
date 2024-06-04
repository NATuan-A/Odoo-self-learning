from odoo import api, fields, models

class ResUsers(models.Model):
    _inherit = "res.users"

    property_ids = fields.One2many(comodel_name="estate.property", inverse_name="salesperson_id",
                                   domain="['|',('state', '=', 'new'),('state','=','offer received')]", string="Properties")

    manager_id = fields.Many2one(comodel_name="res.users", string="Manager")