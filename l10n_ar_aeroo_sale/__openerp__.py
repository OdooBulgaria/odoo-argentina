# -*- coding: utf-8 -*-
{
    'name': 'Argentinian Like Sale Order Aeroo Report',
    'version': '1.0',
    'category': 'Localization/Argentina',
    'sequence': 14,
    'summary': '',
    'description': """
Argentinian Like Sale Order / Quotation Aeroo Report
====================================================
    """,
    'author':  'Ingenieria ADHOC',
    'website': 'www.ingadhoc.com',
    'images': [
    ],
    'depends': [
        'report_extended_sale',
        'l10n_ar_aeroo_base',
        'l10n_ar_aeroo_invoice', #esta dependencia es porque actualizamos algo que crea portal_sale con un valor de las invoice
        'portal_sale',
    ],
    'data': [
        'report_configuration_defaults_data.xml',
        'sale_order_report.xml',
        'sale_order_template.xml',
    ],
    'demo': [
    ],
    'test': [
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: