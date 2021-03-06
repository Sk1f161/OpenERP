# -*- encoding: utf-8 -*-
#########################################################################
#
#    Base scheduler creator module for OpenERP
#    Copyright (C) 2010  Sébastien Beau <sebastien.beau@akretion.com>
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
#########################################################################

from openerp.osv.orm import TransientModel
from openerp.osv.osv import except_osv
from openerp.tools.translate import _

class scheduler_creator_wizard(TransientModel):
    _name = 'scheduler.creator.wizard'
    _description = 'scheduler creator wizard'

    def action_create(self, cr, uid, id, context):
        for id in context['active_ids']:
            if context.get('object_link', False) and self.pool.get(context['object_link']).read(cr, uid, id, ['scheduler'], context)['scheduler']:
                raise except_osv(_('USER ERROR'), _('A scheduler already exists !'))

            vals = {'name':self.pool.get(context['object_link']).read(cr, uid, id, ['name'], context)['name'],
                    'active':False,
                    'user_id':uid,
                    'interval_number':30,
                    'interval_type':'minutes',
                    'numbercall':-1,
                    'doall':False,
                    'model':context['wizard_object'],
                    'function':context['function'],
                    'args':'([' + str(id) +'],)',
                    }
            cron_id = self.pool.get('ir.cron').create(cr, uid, vals, context)
            if context.get('object_link', False):
                self.pool.get(context['object_link']).write(cr, uid, id, {'scheduler' : cron_id}, context)
        return {'type': 'ir.actions.act_window_close'}
