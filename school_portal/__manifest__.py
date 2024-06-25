{
    'name': 'School Portal',
    'version': '1.3',
    'website': 'https://www.odoo.com/app/school',
    'category': 'Services/School',
    'summary': 'Organize and plan your School',
    'depends': [
        'mail',
        'portal',
        'web',
        'school',
    ],
    'data': [
        'views/school_portal_templates.xml',
        'views/school_portal_admission_template.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
