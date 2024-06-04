from odoo import api, fields, models
from datetime import timedelta, date
from odoo.exceptions import UserError


class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Estate Property Offer"
    _order = "price desc"

    price = fields.Float()
    status = fields.Selection(selection=[("accepted", "Accepted"), ("refused", "Refused")], copy=False)
    validity = fields.Integer(default=7)
    date_deadline = fields.Date(compute="_compute_date_deadline", inverse="_inverse_date_deadline")
    property_state_id = fields.Selection(related='property_id.state', string='Property State')

    property_type_id = fields.Many2one(related='property_id.type_id', store=True)
    partner_id = fields.Many2one("res.partner", string="Partner", required=True)
    property_id = fields.Many2one("estate.property", string="Property", required=True)

    @api.model
    def create(self, offer):
        estate_property = self.env['estate.property'].browse(offer['property_id'])
        if offer.get('price') < estate_property.best_price:
            raise UserError("The offer must be higher than {}".format(estate_property.best_price))
        offer_result = super().create(offer)
        offer_result.property_id.state = "offer received"
        return offer_result

    # ---------- Constraints ----------
    _sql_constraints = [
        ('check_price', 'CHECK(price > 0)', 'An offer price must be strictly positive')
    ]

    # ---------- Compute ----------
    @api.depends("validity")
    def _compute_date_deadline(self):
        for record in self:
            record.date_deadline = date.today() + timedelta(days=record.validity)

    # ---------- Inverse ----------
    def _inverse_date_deadline(self):
        for record in self:
            validity_datetime = record.date_deadline - date.today()
            record.validity = validity_datetime.days

    # ---------- Action ----------
    def action_accept_offer(self):
        if self.property_id.state != 'new' and self.property_id.state != 'offer received':
            raise UserError("Cannot accept additional offer")
        self.status = "accepted"
        self.property_id.selling_price = self.price
        self.property_id.buyer_id = self.partner_id
        self.property_id.state = "offer accepted"
        return True

    def action_refuse_offer(self):
        self.status = "refused"
        return True
