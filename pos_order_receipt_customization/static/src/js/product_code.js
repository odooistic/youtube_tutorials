odoo.define('wounded_souls.models', function(require) {
    'use strict';

    var { Orderline } = require('point_of_sale.models');
    var Registries = require('point_of_sale.Registries');

    const CustomOrderline = (Orderline) => class CustomOrderline extends Orderline {
        export_for_printing() {
            var result = super.export_for_printing(...arguments);
            result.default_code = '*' + this.get_product().default_code;
            return result;
        }
    }
    Registries.Model.extend(Orderline, CustomOrderline);
});