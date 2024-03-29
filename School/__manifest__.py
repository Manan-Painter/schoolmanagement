# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'School Management',
    'version': '1.0.0',
    'summary': 'School Management',
    'sequence': 1,
    'website': 'https://www.odoo.com/app/invoicing',
    'description': """
    This is School Managemnt
    """,
    'category': 'School',
    'depends': [],
    'data': [
        'security/ir.model.access.csv',
        'views/student.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
