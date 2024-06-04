from odoo import models, fields, api

class EstateUpdatePriceWizard(models.TransientModel):
    _name = 'estate.update.price.wizard'
    _description = 'Estate Update Price Wizard'

    expected_price = fields.Float(required=True)

    def action_apply(self):
        # Get the active_ids from the context
        active_ids = self.env.context.get('active_ids', [])
        if active_ids:
            # Browse all the records with the active_ids
            records = self.env['estate.property'].browse(active_ids)
            # Update the expected_price for all selected records
            records.write({
                'expected_price': self.expected_price
            })
        return {'type': 'ir.actions.act_window_close'}