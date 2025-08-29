{
    'name': 'Product 101',
    'version': '1.0.0',
    'category': 'Sales',
    'summary': 'Create and display Product 101',
    'description': '''
This addon creates a new product called "Product 101" and provides
a console command to display it.
    ''',
    'author': 'Ernad Husremovic',
    'website': 'https://bring.out.ba',
    'depends': ['base', 'product'],
    'data': [
        'data/product_data.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
