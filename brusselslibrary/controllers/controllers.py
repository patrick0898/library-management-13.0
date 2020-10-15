# -*- coding: utf-8 -*-
# from odoo import http


# class Brusselslibrary(http.Controller):
#     @http.route('/brusselslibrary/brusselslibrary/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/brusselslibrary/brusselslibrary/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('brusselslibrary.listing', {
#             'root': '/brusselslibrary/brusselslibrary',
#             'objects': http.request.env['brusselslibrary.brusselslibrary'].search([]),
#         })

#     @http.route('/brusselslibrary/brusselslibrary/objects/<model("brusselslibrary.brusselslibrary"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('brusselslibrary.object', {
#             'object': obj
#         })
