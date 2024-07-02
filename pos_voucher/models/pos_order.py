from odoo import fields, api, models


class POSOrder(models.Model):
    _inherit = 'pos.order'

    voucher_code = fields.Char(string="Voucher Code")
    voucher_discount = fields.Float(string="Voucher Discount", readonly=True)

    @api.model
    def create(self, vals):
        if vals.get('voucher_code'):
            voucher = self.env['pos.voucher'].search([('code', '=', vals['voucher_code'])], limit=1)
            if voucher:
                vals['voucher_discount'] = voucher.discount
        return super(POSOrder, self).create(vals)