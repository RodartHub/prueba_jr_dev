# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class Myproject(http.Controller):

    @http.route('/myproject/myproject', type='http',auth='public', website=True)

    def index(self, **kw):
        """Resumen:

        Esta funcion evalua si el usuario que accede 
        a esta path està logeado o no por medio de los mètodos http, si està logeado devuelve un hola {nombredeusuario} y si no un hello world
    """
        if request.env.user:
            user = request.env.user
            return f'Hola {user}'

        else:
            return "Hello world!"


