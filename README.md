# S.S Plywood - Product Information System

A web-based product information system for S.S Plywood with role-based access control (Owner and Employee).

## Features

- **User Authentication**: Two user types with different access levels
  - **Owner** (Password: `sshoney`) - Can view all product details including cost price and profit margins
  - **Employee** (Password: `yellow`) - Can view only selling price and stock information
  
- **Product Search**: Search by product number or barcode
- **Barcode Scanner Support**: Compatible with barcode scanners
- **Product Management** (Owner Only): Add, edit, and view all products
- **Excel Data Storage**: All product data stored in `products.xlsx`

## Installation

1. Install required packages:
```bash
pip install -r requirements.txt
```

2. Navigate to the project directory:
```bash
cd ss_plywood
```

## Running the Application

```bash
python app.py
```

The application will start at `http://localhost:5000`

## How to Use

### Login
1. Open the application in your browser
2. Enter password:
   - `sshoney` for Owner access
   - `yellow` for Employee access

### Search for Products (Both Users)
1. After login, you'll see the search page
2. Enter product number (e.g., SSP001) or scan barcode
3. Product details will be displayed based on your user type

### Manage Products (Owner Only)
1. Click "Manage Products" button (visible only for owners)
2. Add new products by filling the form:
   - **Product Number**: Unique identifier (e.g., SSP001)
   - **Barcode**: Barcode number (e.g., 8901234567001)
   - **Product Name**: Name of the product
   - **Price**: Selling price in rupees
   - **Stock**: Quantity in stock
   - **Description**: Product description

3. To update an existing product, use the same Product Number
4. All products are displayed in the table below the form

## Demo Data

The application comes with 6 sample products:

| Product No | Name | Price | Stock |
|---|---|---|---|
| SSP001 | Plywood 6mm Commercial | ₹500 | 100 |
| SSP002 | Plywood 12mm Waterproof | ₹1200 | 75 |
| SSP003 | Plywood 18mm BWR | ₹1800 | 50 |
| SSP004 | Plywood 9mm Standard | ₹750 | 120 |
| SSP005 | Plywood 15mm Marine | ₹1500 | 60 |
| SSP006 | Plywood 21mm Industrial | ₹2100 | 40 |

### Test Barcodes
- SSP001: 8901234567001
- SSP002: 8901234567002
- SSP003: 8901234567003
- SSP004: 8901234567004
- SSP005: 8901234567005
- SSP006: 8901234567006

## Adding Your Own Data

### Method 1: Using the Web Interface (Recommended)
1. Login as Owner (password: `sshoney`)
2. Click "Manage Products"
3. Fill in the product details and click "Save Product"
4. Products are automatically saved to `products.xlsx`

### Method 2: Direct Excel Editing
1. Open `products.xlsx` in Excel or any spreadsheet application
2. Add rows with the following columns:
   - `product_no`: Product identifier
   - `barcode`: Barcode number
   - `name`: Product name
   - `price`: Selling price
   - `stock`: Stock quantity
   - `description`: Product description
3. Save the file
4. Refresh the application

## User-Specific Information Display

### Owner View
- Product Number
- Product Name
- Description
- **Cost Price** (calculated as 80% of selling price)
- **Profit Margin** (20%)
- Selling Price
- Stock
- Barcode

### Employee View
- Product Number
- Product Name
- Description
- **Selling Price Only**
- Stock
- Barcode

## File Structure

```
ss_plywood/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── products.xlsx          # Product database (auto-created)
├── README.md             # This file
└── templates/
    ├── login.html        # Login page
    ├── search.html       # Product search page
    └── manage.html       # Product management page (owner only)
```

## Troubleshooting

### Products not showing up
- Make sure `products.xlsx` exists in the `ss_plywood` directory
- Check that the Excel file has the correct columns: `product_no`, `barcode`, `name`, `price`, `stock`, `description`

### Barcode scanner not working
- Make sure the barcode scanner is configured to send Enter key after scanning
- The search field must be focused when scanning

### Cannot access Manage Products
- Only owners can access this page
- Login with password `sshoney` to access as owner

## Security Notes

- Change the `app.secret_key` in `app.py` to a secure random string for production use
- Passwords are currently hardcoded (for demo purposes only)
- For production, implement proper user authentication with hashed passwords

## Support

For issues or questions, please check the troubleshooting section above.
