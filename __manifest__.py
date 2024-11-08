{
    'name': 'Product Discount Feature',
    'version': '1.0',
    'category': 'Website',
    'summary': 'Add discount field to products and show discounted price on eCommerce store',
    'description': 'Allows setting discount percentages on products and displays the discounted price in the store.',
    'author': 'Jothimani Rajagopal',
    'depends': ['website_sale', 'sale'],
    'data': [
        'views/product_template.xml',
        'views/website_product_templates.xml',
    ],
    'installable': True,
    'application': False,
}
