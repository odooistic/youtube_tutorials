{
    "name": "wounded_souls",
    "version": "23.01",
    "category": "customization",
    "summary": "Wounded Souls General Customization",
    "author": "Odooistic",
    'website': "http://www.odooistic.co.uk/",
    "depends": ['product'],
    "data": [
            'views/product_extension.xml', 
            
    
    ],
    'assets': {
        'point_of_sale.assets': [
            'wounded_souls/static/src/js/**/*',
            'wounded_souls/static/src/xml/**/*',
        ],
    },
    "installable": True,
}

