from odoo import fields, http, SUPERUSER_ID, _
from odoo.http import request

from odoo.addons.portal.controllers import portal
from odoo.addons.portal.controllers.portal import pager as portal_pager
from odoo.exceptions import AccessError, MissingError


class CustomerPortal(portal.CustomerPortal):

    def _prepare_home_portal_values(self, counters):
        values = super()._prepare_home_portal_values(counters)
        values['student_count'] = request.env['school.student'].search_count([]) \
            if request.env['school.student'].check_access_rights('read', raise_exception=False) else 0

        return values

    def _prepare_student_domain(self):
        return []

    def _prepare_searchbar_sortings(self):
        return {
            'date': {'label': _('Newest'), 'order': 'create_date desc'},
            'name': {'label': _('Name'), 'order': 'name'},
        }

    @http.route(['/my/students', '/my/students/page/<int:page>'], type='http', auth="user", website=True)
    def portal_my_students(self, page=1, date_begin=None, date_end=None, sortby=None, **kw):
        values = self._prepare_portal_layout_values()
        Student = request.env['school.student']
        domain = self._prepare_student_domain()

        searchbar_sortings = self._prepare_searchbar_sortings()
        if not sortby or sortby not in searchbar_sortings:
            sortby = 'date'
        order = searchbar_sortings[sortby]['order']

        student_count = Student.search_count(domain)
        # pager
        pager = portal_pager(
            url="/my/students",
            url_args={'date_begin': date_begin, 'date_end': date_end, 'sortby': sortby},
            total=student_count,
            page=page,
            step=self._items_per_page
        )

        # content according to pager and archive selected
        students = Student.search(domain, order=order, limit=self._items_per_page, offset=pager['offset'])
        request.session['my_student_history'] = students.ids[:100]

        values.update({
            'date': date_begin,
            'date_end': date_end,
            'students_list': students,
            'page_name': 'student',
            'default_url': '/my/students',
            'pager': pager,
            'searchbar_sortings': searchbar_sortings,
            'sortby': sortby
        })
        return request.render("school.portal_my_students", values)

    def _show_student_report(self, student_sudo, report_type, download):
        raise MissingError(_('There is nothing to report.'))

    def _student_get_page_view_values(self, student, access_token, **kwargs):
        page_name = 'student'
        history = 'my_student_history'
        try:
            student_accessible = bool(self._document_check_access('school.student', student.id))
        except (AccessError, MissingError):
            student_accessible = False
        values = {
            'page_name': page_name,
            'student': student,
            'user': request.env.user,
            'student_accessible': student_accessible,
        }

        values = self._get_page_view_values(student, access_token, values, history, False, **kwargs)
        return values

    @http.route(['/my/students/<int:student>'], type='http', auth="public", website=True)
    def portal_my_student_view(self, student, access_token=None, **kw):
        try:
            student_sudo = self._document_check_access('school.student', student, access_token=access_token)
        except (AccessError, MissingError):
            return request.redirect('/my')

        report_type = kw.get('report_type')
        if report_type in ('html', 'pdf', 'text'):
            return self._show_report(model=student_sudo, report_type=report_type,
                                     report_ref='school.action_report_school_student', download=kw.get('download'))

        # ensure attachment are accessible with access token inside template
        values = self._student_get_page_view_values(student_sudo, access_token, **kw)
        return request.render("school.portal_my_student_view", values)
