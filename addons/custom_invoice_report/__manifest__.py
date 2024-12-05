{
    'name': 'Custom Invoice Report',
    'version': '1.0',
    'summary': 'A custom invoice report layout',
    'author': 'Your Name',
    'category': 'Reporting',
    'depends': ['base', 'account', 'sale'],  # Add 'sale' or other modules if needed
    'data': [
        'reports/custom_invoice_template.xml',
        'views/invoice_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': True,
}
