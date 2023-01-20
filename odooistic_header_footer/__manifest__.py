{
    "name": "odooistic_report_template",
    "version": "14.01",
    "category": "Tools",
    "summary": "Custom Report Header & Footer for Odooistic",
    "author": "Odooistic",
    'website': "http://www.odooistic.co.uk/",
    "depends": ["base"],
    "data": [
            "views/template.xml", 
            # "views/assets.xml",
    ],
    'assets': {
        'web.report_assets_common': [
            'odooistic_header_footer/static/src/scss/**/*',
        ],
    },
    "installable": True,
}

