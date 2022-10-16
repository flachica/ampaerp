import random
import string

from odoo import api, models


class MembershipLine(models.Model):
    _inherit = "membership.membership_line"

    @api.model
    def create(self, vals):
        partner_model = self.env["res.partner"]
        member_id = partner_model.browse(vals["partner"])
        if not member_id.ref:
            reference = "".join(random.choices(string.ascii_letters, k=7)).upper()
            partner_id = self.env["res.partner"].search([("ref", "=", reference)])
            while partner_id:
                reference = "".join(random.choices(string.ascii_letters, k=7)).upper()
                partner_id = self.env["res.partner"].search([("ref", "=", reference)])
            member_id.ref = reference
        return super(MembershipLine, self).create(vals)
