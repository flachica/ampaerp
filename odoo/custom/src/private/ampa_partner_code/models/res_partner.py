from odoo import models


class ResPartner(models.Model):
    _inherit = "res.partner"

    def action_open_membership_layout(self):
        action = self.env["ir.actions.act_window"]._for_xml_id(
            "ampa_partner_code.action_open_membership_layout"
        )
        action["context"] = {"default_partner_ids": self.ids}
        return action
