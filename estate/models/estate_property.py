from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate Property"
    _order = "id desc"

    name = fields.Char(string="Title", required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(string="Available From", default=fields.Date.today, copy=False)
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(default=1)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean(string="Garage")
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(string="Garden Orientation",
                                          selection=[("N", "North"), ("S", "South"), ("E", "East"),
                                                     ("W", "West")])
    active = fields.Boolean(default=False)
    state = fields.Selection(string="Status", required=True, copy=False, default="new",
                             selection=[("new", "New"), ("offer received", "Offer Received"),
                                        ("offer accepted", "Offer Accepted"), ("sold", "Sold"),
                                        ("canceled", "Canceled")])
    total_area = fields.Integer(compute="_compute_total")
    best_price = fields.Float(compute="_compute_best_price", string="Best Offer")

    salesperson_id = fields.Many2one('res.users', string='Salesperson', default=lambda self: self.env.user)
    buyer_id = fields.Many2one('res.partner', string='Buyer', copy=False)
    type_id = fields.Many2one('estate.property.type', string='Property Type')
    tag_ids = fields.Many2many("estate.property.tag", string="Property Tags")
    offer_ids = fields.One2many("estate.property.offer", "property_id", string="Property Offers")

    # ---------- Override ----------
    @api.ondelete(at_uninstall=False)
    def _unlink_if_not_canceled_or_new_property(self):
        if any(estate_property.state not in ["new", "canceled"] for estate_property in self):
            raise UserError("Only new and canceled properties can be deleted!")

    # ---------- Constraints ----------
    _sql_constraints = [
        ('check_expected_price', 'CHECK(expected_price > 0)', 'A expected price must be strictly positive'),
        ('check_selling_price', 'CHECK(selling_price > 0)', 'A selling price must be positive')
    ]

    @api.constrains('selling_price')
    def _check_date_end(self):
        for record in self:
            if record.selling_price < record.expected_price * 0.9:
                raise ValidationError("The selling price must be at least 90% of the expected price! You must reduce the expected price if you want to accept this offer.")

    # ---------- Compute ----------
    @api.depends("living_area", "garden_area")
    def _compute_total(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    @api.depends("offer_ids.price")
    def _compute_best_price(self):
        for record in self:
            record.best_price = max([0, *record.offer_ids.mapped("price")])  # offer.price for offer in record.offer_ids

    # ---------- Onchange ----------
    @api.onchange("garden")
    def _onchange_garden(self):
        if self.garden:
            self.garden_area = 10
            self.garden_orientation = "north"
        else:
            self.garden_area = 0
            self.garden_orientation = ""

    # ---------- Action ----------
    def action_sold_property(self):
        if self.state == 'cancel':
            raise UserError("A canceled property cannot be sold")
        self.state = 'sold'
        return True

    def action_canceled_property(self):
        if self.state == 'sold':
            raise UserError("A sold property cannot be canceled")
        self.state = 'cancel'
        return True
