from odoo import http
from odoo.http import request


class SimpleIndex(http.Controller):

    @http.route('/simple_index', type='http', auth='public', website=True)
    def index(self, **kwargs):
        return request.render('simple_index.index_template', {})
