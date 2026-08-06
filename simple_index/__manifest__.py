{
    'name': 'Simple Index',
    'version': '19.0.1.0.0',
    'summary': 'A minimal module that only shows an index page',
    'description': """
Simple Index
============
A bare-bones Odoo 19 module containing only a single controller
that renders an "index" page at /simple_index.
""",
    'author': 'Your Name',
    'category': 'Website',
    'license': 'LGPL-3',
    'depends': ['website'],
    'data': [
        'views/index_template.xml',
    ],
    'installable': True,
    'application': False,
}
