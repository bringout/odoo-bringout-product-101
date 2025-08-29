# Odoo Bringout Product 101

A simple Odoo addon that demonstrates pythonic Odoo development by creating a product called "Product 101" and providing a console command to display it.

## Features

- Creates a product named "Product 101" with predefined attributes
- Provides a console command `odoo-product-101` to show product details
- Includes comprehensive tests
- Follows pythonic package structure

## Installation

```bash
pip install odoo-bringout-product-101
```

## Usage

### Console Command

After installation, you can display Product 101 details:

```bash
# Set your database name (optional, defaults to 'odoo')
export ODOO_DATABASE=your_database_name

# Show Product 101 details
odoo-product-101
```

### In Odoo

1. Install the addon through Odoo's addon manager
2. The product "Product 101" will be automatically created
3. You can find it in Sales → Products → Products

## Product Details

- **Name**: Product 101  
- **Price**: $101.00
- **Cost**: $50.00
- **Code**: PROD-101
- **Type**: Consumable
- **Description**: Demo product created by pythonic Odoo development

## Development

This package demonstrates:

- Pythonic Odoo addon structure
- Using `pyproject.toml` for configuration
- Console script integration
- Proper test coverage
- Data files for initial data loading

## Testing

Run tests with:

```bash
# In Odoo test environment
odoo -d test_database -i product_101 --test-enable --stop-after-init
```

## Dependencies

- odoo-bringout-oca-ocb-base>=16.0.0
- odoo-bringout-oca-ocb-addons-product>=16.0.0

## License

LGPL-3

## Documentation

- Overview: doc/OVERVIEW.md
- Architecture: doc/ARCHITECTURE.md
- Models: doc/MODELS.md
- Controllers: doc/CONTROLLERS.md
- Wizards: doc/WIZARDS.md
- Install: doc/INSTALL.md
- Usage: doc/USAGE.md
- Configuration: doc/CONFIGURATION.md
- Dependencies: doc/DEPENDENCIES.md
- Troubleshooting: doc/TROUBLESHOOTING.md
- FAQ: doc/FAQ.md
