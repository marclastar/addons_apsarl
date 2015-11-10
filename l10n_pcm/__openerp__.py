# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2015 AFRICA PERFORMANCES (<www.africaperformances-ci.com>).
#    contact: infos@africaperformances-ci.com
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
    'name' : 'PCM 2015 - Accounting Mauritania by Africa Performances',
    'version' : '1.0',
    'author' : 'Africa Performances',
    'category' : 'Localization/Account Charts',
    'description': 	"""
					Accounting chart PCM for Mauritania.
					- Account type from Annual Financial Statement (TO DO)
					- VAT Taxes and Fiscal Position for Ivory Coast (TO DO)
					""",
    'website': 'http://www.africaperformances-ci.com/',
	'license': 'AGPL-3'
    'depends' : ['account', 'base_vat'],
    'demo' : [],
    'data' : ['l10n_pcm_data.xml','l10n_pcm_wizard.xml'],
    'auto_install': False,
    'installable': True
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
