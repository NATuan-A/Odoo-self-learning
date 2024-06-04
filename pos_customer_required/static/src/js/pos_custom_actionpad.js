odoo.define('custom_pos.ActionpadWidget', function(require) {
    "use strict";

    const ActionpadWidget = require('point_of_sale.ActionpadWidget');
    const Registries = require('point_of_sale.Registries');

    const CustomActionpadWidget = (ActionpadWidget) =>
        class extends ActionpadWidget {
            async startPayment() {
                const order = this.env.pos.get_order();
                if (this.env.pos.config.customer_required && !order.get_client()) {
                    this.showPopup('ErrorPopup', {
                        title: this.env._t('Customer Required'),
                        body: this.env._t('Please select a customer before proceeding with the payment.'),
                    });
                    return;
                }
                super.startPayment();
            }
        };

    Registries.Component.extend(ActionpadWidget, CustomActionpadWidget);

    return ActionpadWidget;
});
