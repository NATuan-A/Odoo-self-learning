from odoo import api, fields, models


class EstateProperty(models.Model):
    _name = "pos.voucher"
    _description = "POS Voucher"

    code = fields.Char(string="Voucher CODE", required=True)
    discount = fields.Float(string="Discount Percentage", required=True)