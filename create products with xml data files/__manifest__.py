{

    'name': 'Odooistic',
    'version': '1.2',
    'summary': 'Odooistic Customization',
    'sequence': 30,
    
    'description': """
    Long Description of your modules""",
    'author': 'Odooistic',
    'company': 'Company Name',
    'website': 'https://www.website.com',
    'category': 'Customization',
    'depends': ['base', 'project', 'sale', 'mail', 'purchase','product'],
    'data': [
        'data/product_data.xml',
        'security/ir.model.access.csv',
        'views/project_task.xml',
        'views/sale_order_extension.xml',
        'views/purchase_order_ext.xml',
        'views/partner_hobbies.xml',
        'reports/sale_report_ext.xml',

   ],
    'application': True,
}