# -*- coding: utf-8 -*-
# © 2015 Grupo ESOC Ingeniería de Servicios, S.L.U. - Jairo Llopis
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Snippet Background Style",
    "summary": "Let you change styles of snippets background images",
    "version": "8.0.1.0.0",
    "category": "Website",
    "website": "https://odoo-community.org/",
    "author": "Grupo ESOC, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "external_dependencies": {
        "python": [],
        "bin": [],
    },
    "depends": [
        "website",
    ],
    "data": [
        "views/assets.xml",
        "views/snippets.xml",
    ],
}
