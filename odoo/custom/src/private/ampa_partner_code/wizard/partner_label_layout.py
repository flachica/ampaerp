from odoo import api, fields, models


class PartnerLabelLayout(models.TransientModel):
    _name = "partner.label.layout"
    _description = "Choose the sheet layout to print the mebership card"

    print_format = fields.Selection(
        [
            ("2x7", "2 x 7"),
            ("4x7", "4 x 7"),
            ("4x12", "4 x 12"),
        ],
        string="Format",
        default="2x7",
        required=True,
    )
    partner_ids = fields.Many2many("res.partner")
    rows = fields.Integer(compute="_compute_dimensions")
    columns = fields.Integer(compute="_compute_dimensions")

    @api.depends("print_format")
    def _compute_dimensions(self):
        for wizard in self:
            if "x" in wizard.print_format:
                columns, rows = wizard.print_format.split("x")[:2]
                wizard.columns = int(columns)
                wizard.rows = int(rows)
            else:
                wizard.columns, wizard.rows = 1, 1

    def process(self):
        self.ensure_one()
        xml_id = "ampa_partner_code.report_partner_card"
        data = {
            "active_model": "res.partner",
            "layout_wizard": self.id,
        }
        report_action = self.env.ref(xml_id).report_action(None, data=data)
        report_action.update({"close_on_report_download": True})
        return report_action


# report_product_template_label
