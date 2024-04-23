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
    'depends': ["sale","mail"],
    'data': [
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'data/ir_sequence_addmission_data.xml',
        'data/ir_sequence_teacher_data.xml',
        'data/ir_sequence_peon_data.xml',
        'data/ir_sequence_guardian_data.xml',
        'views/student.xml',
        'views/student_list.xml',
        'views/teacher.xml',
        'views/peon.xml',
        'views/guardian.xml',
        'views/attendance_student.xml',
        'views/attendance_teacher.xml',
        'views/attendance_guardian.xml',
        'views/attendance_peon.xml',
        'views/school_book.xml',
        # 'views/student_time_table.xml',
        # 'views/teacher_time_table.xml',
        # 'views/semester_fees.xml',
        # 'views/bus_fees.xml',
        # 'views/exam_fees.xml',
        # 'views/books_fees.xml',
        # 'views/exam_form.xml',
        # 'views/hall_ticket.xml',
        # 'views/exam_attendance.xml',
        'views/result.xml',
        # 'views/assignment.xml',
        # 'views/submission.xml',
        'views/menu.xml',
        'views/base_class.xml',
        "views/sale_order_view.xml",
        "views/res_partener.xml",
        "views/product.xml",
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}


