/** @odoo-module */

import { Component } from "@odoo/owl";
import { registry } from "@web/core/registry";

export class SeedsHome extends Component {
    static template = "seeds.HomeScreen";
}

registry.category("actions").add("seeds.home", SeedsHome);