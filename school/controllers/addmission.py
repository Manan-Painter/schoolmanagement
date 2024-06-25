from odoo import fields, http, SUPERUSER_ID, _
from odoo.http import request

from odoo.addons.portal.controllers import portal
from odoo.addons.portal.controllers.portal import pager as portal_pager


class CustomerPortal(portal.CustomerPortal):

    def _prepare_home_portal_values(self, counters):
        values = super()._prepare_home_portal_values(counters)
        values['admission_count'] = request.env['admission.student'].search_count([]) \
            if request.env['admission.student'].check_access_rights('read', raise_exception=False) else 0
        return values

    def _prepare_admission_domain(self):
        return []

    def _prepare_admission_searchbar_sortings(self):
        return {
            'date': {'label': _('Newest'), 'order': 'create_date desc'},
            'name': {'label': _('Name'), 'order': 'name'},
        }

    @http.route(['/my/admission', '/my/admission/page/<int:page>'], type='http', auth="user", website=True)
    def portal_my_admission(self, page=1, date_begin=None, date_end=None, sortby=None, **kw):
        values = self._prepare_portal_layout_values()
        Admission = request.env['admission.student']
        domain = self._prepare_admission_domain()

        searchbar_sortings = self._prepare_admission_searchbar_sortings()
        if not sortby or sortby not in searchbar_sortings:
            sortby = 'date'
        order = searchbar_sortings[sortby]['order']

        admission_count = Admission.search_count(domain)
        # pager
        pager = portal_pager(
            url="/my/admission",
            url_args={'date_begin': date_begin, 'date_end': date_end, 'sortby': sortby},
            total=admission_count,
            page=page,
            step=self._items_per_page
        )

        # content according to pager and archive selected
        admissions = Admission.search(domain, order=order, limit=self._items_per_page, offset=pager['offset'])
        request.session['my_admission_history'] = admissions.ids[:100]

        values.update({
            'date': date_begin,
            'date_end': date_end,
            'admissions': admissions,
            'page_name': 'admission',
            'default_url': '/my/admission',
            'pager': pager,
            'searchbar_sortings': searchbar_sortings,
            'sortby': sortby
        })
        return request.render("school.portal_my_admission", values)

