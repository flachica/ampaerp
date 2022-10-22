# Copyright Fernando La Chica <fernandolachica@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Partner Code",
    "summary": "Add a code field to partners and generate random when is a member",
    "version": "15.0.1.0.0",
    "author": "Fernando La Chica" "Odoo Community Association (OCA)",
    "category": "membership",
    "license": "AGPL-3",
    "website": "https://github.com/flachica/ampaerp",
    "depends": ["membership"],
    "data": [
        "security/ir.model.access.csv",
        "views/partner_reports.xml",
        "views/membership_views.xml",
        "wizard/partner_label_layout_views.xml",
    ],
    "maintainers": ["flachica"],
    "application": False,
    "installable": True,
}
