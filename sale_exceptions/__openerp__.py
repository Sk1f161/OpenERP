# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2011 Akretion LTDA.
#    authors: Raphaël Valyi, Renato Lima
#    Copyright (C) 2010-2012 Akretion Sébastien BEAU <sebastien.beau@akretion.com>
#    Copyright (C) 2012 Camptocamp SA (Guewen Baconnier)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


{
    'name': 'Sale Exceptions',
    'version': '2.0',
    'category': 'Generic Modules/Sale',
    'description': """
This module allows you attach several customizable exceptions to your sale order in a way that you can filter orders by exceptions type and fix them.
This is especially useful in an order importation scenario such as with the base_sale_multi_channels module, because it's likely a few orders have errors when you import them (like product not found in OpenERP, wrong line format etc...)
""",
    'author': 'Akretion',
    'website': 'http://www.akretion.com',
    'depends': [
        'sale',
        'email_template'
    ],
    'init_xml': [
                   'settings/sale.exception.csv',
                ],
    'update_xml': ['sale_workflow.xml',
                   'sale_view.xml',
                   'sale_exceptions_data.xml',
                   'wizard/sale_exception_confirm_view.xml',
                   'security/ir.model.access.csv',
                   'sale_exceptions_mail_template.xml',
                   ],
    'demo_xml': [],
    'installable': True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
