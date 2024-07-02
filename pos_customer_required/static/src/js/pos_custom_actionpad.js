odoo.define('custom_pos.ProductScreen', function(require) {
    "use strict";

    const ProductScreen = require('point_of_sale.ProductScreen');
    const Registries = require('point_of_sale.Registries');

    const CustomProductScreen = (ProductScreen) =>
        class extends ProductScreen {
            async _onClickPay() {
                const order = this.env.pos.get_order();
                if (this.env.pos.config.customer_required && !order.get_partner()) {
                    this.showPopup('ErrorPopup', {
                        title: this.env._t('Customer Required'),
                        body: this.env._t('Please select a customer before proceeding with the payment.'),
                    });
                    return;
                }
                super._onClickPay();
            }
        };

    Registries.Component.extend(ProductScreen, CustomProductScreen);

    return ProductScreen;
});
