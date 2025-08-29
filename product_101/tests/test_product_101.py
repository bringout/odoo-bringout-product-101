from odoo.tests.common import TransactionCase

class TestProduct101(TransactionCase):
    
    def setUp(self):
        super().setUp()
        self.ProductTemplate = self.env['product.template']
    
    def test_create_product_101(self):
        '''Test creating Product 101.'''
        # Ensure product doesn't exist initially
        existing = self.ProductTemplate.search([('name', '=', 'Product 101')])
        existing.unlink()  # Remove if exists
        
        # Create product
        product = self.ProductTemplate.create_product_101()
        
        # Verify product was created
        self.assertTrue(product)
        self.assertEqual(product.name, 'Product 101')
        self.assertEqual(product.list_price, 101.00)
        self.assertEqual(product.default_code, 'PROD-101')
    
    def test_show_product_101(self):
        '''Test showing Product 101 details.'''
        # Ensure product exists
        self.ProductTemplate.create_product_101()
        
        # Show product details
        details = self.ProductTemplate.show_product_101()
        
        # Verify details
        self.assertIsNotNone(details)
        self.assertEqual(details['name'], 'Product 101')
        self.assertEqual(details['price'], 101.00)
        self.assertEqual(details['code'], 'PROD-101')
    
    def test_product_101_data_loaded(self):
        '''Test that Product 101 is loaded from data file.'''
        # Product should exist from data file
        product = self.ProductTemplate.search([('name', '=', 'Product 101')], limit=1)
        
        self.assertTrue(product, "Product 101 should be loaded from data file")
        self.assertEqual(product.list_price, 101.00)
        self.assertEqual(product.standard_price, 50.00)
