##############################################################################
#
# Copyright (c) 2010-2012 NaN Projectes de Programari Lliure, S.L.
#                         All Rights Reserved.
#                         http://www.NaN-tic.com
#
# WARNING: This program as such is intended to be used by professional
# programmers who take the whole responsability of assessing all potential
# consequences resulting from its eventual inadequacies and bugs
# End users who are looking for a ready-to-use solution with commercial
# garantees and support are strongly adviced to contract a Free Software
# Service Company
#
# This program is Free Software; you can redistribute it and/or
# modify it under the terms of the GNU Affero General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#
##############################################################################

{
    "name": "Production Lot Quality Control - Production",
    "version": "1.0",
    "author": "NaN·tic",
    "category": "Quality Control",
    "website": "http://www.nan-tic.com",
    "description": """
    This module adds quality control to Production Lots on production (in
    produced Lots).
    """,
    "depends": [
        'oo_nan_prodlot_quality_control',
        'mrp',
    ],
    "init_xml": [],
    "update_xml": [
        'quality_control_data.xml',
    ],
    "demo_xml": [
        'prodlot_quality_control_production_demo.xml',
    ],
    "test": [
        'test/prodlot_qc_production_wo_tests.yml',
        'test/prodlot_qc_production_w_1_test.yml',
        'test/prodlot_qc_production_w_2_tests.yml',
    ],
    "active": False,
    "installable": True,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
