from odoo import fields, models


class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "Estate Property Tag"
    _order = "name"

    name = fields.Char(required=True)
    color = fields.Integer()

    # ---------- Constraints ----------
    _sql_constraints = [
        ('name_unique', 'unique(name)', 'A property tag name must be unique')
    ]