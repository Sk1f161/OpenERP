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

{
    "name" : "base_scheduler_creator",
    "version" : "6.1.0",
    "license": "AGPL-3",
    "depends" : ["base"],
    "author" : "Akretion",
    "description": """Allows the automatic creation of a scheduler.""",
    "website" : "http://www.akretion.com/",
    "category" : "Generic Modules/Other",
    "init_xml" : [],
    "demo_xml" : [],
    "update_xml" : ["schedulder_creator.xml"],
    "active": False,
    "installable": False,
}
