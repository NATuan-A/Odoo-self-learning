odoo.define('pos_voucher.models', function(require) {
    "use strict";

    const models = require('point_of_sale.models');
    const Order = models.Order;
    const OrderSuper = Order.prototype;

    models.load_fields('pos.order', ['voucher_code', 'voucher_discount']);

    models.Order = Order.extend({
        initialize: function(attr, options) {
            OrderSuper.initialize.call(this, attr, options);
            this.voucher_code = this.voucher_code || '';
            this.voucher_discount = this.voucher_discount || 0;
        },

        apply_voucher: function(voucher_code) {
            let voucher = this.pos.vouchers.find(v => v.code === voucher_code);
            if (voucher) {
                this.voucher_code = voucher.code;
                this.voucher_discount = voucher.discount;
                this.trigger('change', this);
            } else {
                this.voucher_code = '';
                this.voucher_discount = 0;
                this.trigger('change', this);
                this.pos.gui.show_popup('error', {
                    'title': 'Invalid Voucher',
                    'body': 'The voucher code is invalid.',
                });
            }
        },

        export_as_JSON: function() {
            let json = OrderSuper.export_as_JSON.apply(this, arguments);
            json.voucher_code = this.voucher_code;
            json.voucher_discount = this.voucher_discount;
            return json;
        },

        init_from_JSON: function(json) {
            OrderSuper.init_from_JSON.apply(this, arguments);
            this.voucher_code = json.voucher_code;
            this.voucher_discount = json.voucher_discount;
        }
    });

    models.load_models({
        model: 'pos.voucher',
        fields: ['code', 'discount'],
        loaded: function(self, vouchers) {
            self.vouchers = vouchers;
        }
    });
});
