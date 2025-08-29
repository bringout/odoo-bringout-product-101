#!/usr/bin/env python3
'''Console command to show Product 101 details.'''

import sys
import os
import odoo
from odoo import api

def show():
    '''Main function to show Product 101 details.'''
    # Initialize Odoo
    odoo.tools.config.parse_config([])
    
    # Get database name from environment or use default
    db_name = os.environ.get('ODOO_DATABASE', 'odoo')
    
    try:
        # Create database registry and environment
        registry = odoo.registry(db_name)
        with api.Environment.manage():
            with registry.cursor() as cr:
                env = api.Environment(cr, odoo.SUPERUSER_ID, {})
                
                # Get product template model and show Product 101
                ProductTemplate = env['product.template']
                result = ProductTemplate.show_product_101()
                
                if result:
                    return 0
                else:
                    return 1
                    
    except Exception as e:
        print(f"Error: {e}")
        print("Make sure:")
        print("1. Odoo database is created and accessible")
        print("2. Product 101 addon is installed")
        print("3. ODOO_DATABASE environment variable is set (optional)")
        return 1

if __name__ == '__main__':
    sys.exit(show())
