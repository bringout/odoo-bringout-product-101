from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    def create_product_101(self):
        '''Create Product 101 if it doesn't exist.'''
        existing_product = self.search([('name', '=', 'Product 101')])
        if not existing_product:
            product = self.create({
                'name': 'Product 101',
                'type': 'consu',
                'list_price': 101.00,
                'standard_price': 50.00,
                'description': 'This is Product 101 - a demo product created by pythonic Odoo development',
                'default_code': 'PROD-101',
            })
            _logger.info(f"Created Product 101 with ID: {product.id}")
            return product
        else:
            _logger.info(f"Product 101 already exists with ID: {existing_product.id}")
            return existing_product

    @api.model
    def show_product_101(self):
        '''Show Product 101 details.'''
        product = self.search([('name', '=', 'Product 101')], limit=1)
        if product:
            details = {
                'id': product.id,
                'name': product.name,
                'price': product.list_price,
                'cost': product.standard_price,
                'code': product.default_code,
                'description': product.description,
            }
            _logger.info(f"Product 101 details: {details}")
            print(f"\n=== Product 101 Details ===")
            print(f"ID: {details['id']}")
            print(f"Name: {details['name']}")
            print(f"Price: ${details['price']:.2f}")
            print(f"Cost: ${details['cost']:.2f}")
            print(f"Code: {details['code']}")
            print(f"Description: {details['description']}")
            print(f"===========================\n")
            return details
        else:
            _logger.warning("Product 101 not found!")
            print("Product 101 not found! Please install the addon data first.")
            return None
