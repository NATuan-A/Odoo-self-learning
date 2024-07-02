odoo.define('pos_voucher.VoucherButton', function(require) {
    "use strict";

    const PosComponent = require('point_of_sale.PosComponent');
    const ProductScreen = require('point_of_sale.ProductScreen');
    const Registries = require('point_of_sale.Registries');
    const { useListener } = require("@web/core/utils/hooks");

    class VoucherButton extends PosComponent {
        setup() {
            super.setup();
            useListener('click', this.onClick);
        }

        async onClick() {
            console.log("CLICK");
        }
    }

    VoucherButton.template = 'VoucherButton';

    ProductScreen.addControlButton({
        component: VoucherButton,
        position: ['before', 'SetFiscalPositionButton'],
    });

    Registries.Component.add(VoucherButton);

    return VoucherButton;
});
