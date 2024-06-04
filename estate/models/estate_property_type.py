from odoo import api, fields, models


class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Estate Property Type"
    _order = "sequence, name"

    name = fields.Char(required=True)
    offer_count = fields.Integer(compute="_compute_offer_count")
    sequence = fields.Integer('Sequence', default=1, help="Used to order stages. Lower is better.")

    property_ids = fields.One2many("estate.property", "type_id", string="Properties")
    offer_ids = fields.One2many("estate.property.offer", "property_type_id")

    # ---------- Compute ----------
    @api.depends("offer_ids")
    def _compute_offer_count(self):
        for record in self:
            record.offer_count = len(record.offer_ids)

    # ---------- Constraints ----------
    _sql_constraints = [
        ('name_unique', 'unique(name)', 'A property type name must be unique')
    ]
