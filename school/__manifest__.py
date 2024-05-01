# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'school Management',
    'version': '1.0.0',
    'summary': 'school Management',
    'sequence': 1,
    'website': 'https://www.odoo.com/app/invoicing',
    'description': """
    This is school Managemnt
    """,
    'category': 'school',
    'depends': ["sale","mail","purchase"],
    'data': [
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'data/ir_sequence_addmission_data.xml',
        'data/ir_sequence_teacher_data.xml',
        'data/ir_sequence_peon_data.xml',
        'data/ir_sequence_guardian_data.xml',
        "wizard/student_last_school_info_view.xml",
        'views/student.xml',
        'views/admission.xml',
        'views/teacher_staff.xml',
        'views/peon_staff.xml',
        'views/guardian_staff.xml',
        'views/attendance_student.xml',
        'views/attendance_teacher.xml',
        'views/attendance_guardian.xml',
        'views/attendance_peon.xml',
        'views/school_book.xml',
        'views/menu.xml',
        "views/sale_order_view.xml",
        "views/res_partener.xml",
        "views/product.xml",
        "views/average_grade.xml",
        "views/purchase_order.xml",
        "wizard/admission_cancle_info_view.xml",
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}


