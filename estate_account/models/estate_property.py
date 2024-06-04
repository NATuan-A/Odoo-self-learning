from odoo import api, fields, models, Command


class EstateProperty(models.Model):
    _inherit = "estate.property"

    def action_sold_property(self):
        temp = self.env['account.move'].create({
            'name': 'Invoice',
            'move_type': 'out_receipt',
            'partner_id': self.buyer_id.id,
            "invoice_line_ids": [
                Command.create({
                    "name": self.name,
                    "quantity": 1,
                    "price_unit": self.selling_price
                })
            ],
        })
        return super().action_sold_property()
