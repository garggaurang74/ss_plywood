from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import pandas as pd
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Change this to a secure secret key

# Excel file path
EXCEL_FILE = 'products.xlsx'
CREDENTIALS_FILE = 'credentials.xlsx'

# Create sample Excel file with separate sheets if it doesn't exist
if not os.path.exists(EXCEL_FILE):
    owner_data = pd.DataFrame([
        {'product_no': 'SSP001', 'barcode': '8901234567001', 'name': 'Plywood 6mm Commercial', 'price': 500, 'cost_price': 400, 'stock': 100, 'description': '6mm Commercial Grade Plywood - Standard Quality'},
        {'product_no': 'SSP002', 'barcode': '8901234567002', 'name': 'Plywood 12mm Waterproof', 'price': 1200, 'cost_price': 960, 'stock': 75, 'description': '12mm Waterproof Grade Plywood - Premium Quality'},
        {'product_no': 'SSP003', 'barcode': '8901234567003', 'name': 'Plywood 18mm BWR', 'price': 1800, 'cost_price': 1440, 'stock': 50, 'description': '18mm BWR Grade Plywood - Heavy Duty'},
        {'product_no': 'SSP004', 'barcode': '8901234567004', 'name': 'Plywood 9mm Standard', 'price': 750, 'cost_price': 600, 'stock': 120, 'description': '9mm Standard Grade Plywood - General Purpose'},
        {'product_no': 'SSP005', 'barcode': '8901234567005', 'name': 'Plywood 15mm Marine', 'price': 1500, 'cost_price': 1200, 'stock': 60, 'description': '15mm Marine Grade Plywood - Weather Resistant'},
        {'product_no': 'SSP006', 'barcode': '8901234567006', 'name': 'Plywood 21mm Industrial', 'price': 2100, 'cost_price': 1680, 'stock': 40, 'description': '21mm Industrial Grade Plywood - High Strength'},
    ])
    
    employee_data = pd.DataFrame([
        {'product_no': 'SSP001', 'barcode': '8901234567001', 'name': 'Plywood 6mm Commercial', 'price': 500, 'stock': 100, 'description': '6mm Commercial Grade Plywood - Standard Quality'},
        {'product_no': 'SSP002', 'barcode': '8901234567002', 'name': 'Plywood 12mm Waterproof', 'price': 1200, 'stock': 75, 'description': '12mm Waterproof Grade Plywood - Premium Quality'},
        {'product_no': 'SSP003', 'barcode': '8901234567003', 'name': 'Plywood 18mm BWR', 'price': 1800, 'stock': 50, 'description': '18mm BWR Grade Plywood - Heavy Duty'},
        {'product_no': 'SSP004', 'barcode': '8901234567004', 'name': 'Plywood 9mm Standard', 'price': 750, 'stock': 120, 'description': '9mm Standard Grade Plywood - General Purpose'},
        {'product_no': 'SSP005', 'barcode': '8901234567005', 'name': 'Plywood 15mm Marine', 'price': 1500, 'stock': 60, 'description': '15mm Marine Grade Plywood - Weather Resistant'},
        {'product_no': 'SSP006', 'barcode': '8901234567006', 'name': 'Plywood 21mm Industrial', 'price': 2100, 'stock': 40, 'description': '21mm Industrial Grade Plywood - High Strength'},
    ])
    
    with pd.ExcelWriter(EXCEL_FILE, engine='openpyxl') as writer:
        owner_data.to_excel(writer, sheet_name='owner', index=False)
        employee_data.to_excel(writer, sheet_name='employee', index=False)

# Create credentials file if it doesn't exist
if not os.path.exists(CREDENTIALS_FILE):
    credentials = pd.DataFrame([
        {'user_type': 'owner', 'password': 'sshoney'},
        {'user_type': 'employee', 'password': 'yellow'}
    ])
    credentials.to_excel(CREDENTIALS_FILE, index=False)

def get_product_info(identifier, user_type='employee'):
    try:
        # Read from the appropriate sheet based on user type
        sheet_name = 'owner' if user_type == 'owner' else 'employee'
        df = pd.read_excel(EXCEL_FILE, sheet_name=sheet_name)
        
        # Try to find by product number
        product = df[df['product_no'].str.lower() == identifier.lower()]
        if product.empty:
            # If not found by product number, try barcode
            product = df[df['barcode'].astype(str) == identifier]
        
        if not product.empty:
            return product.iloc[0].to_dict()
        return None
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return None

def get_credentials():
    try:
        df = pd.read_excel(CREDENTIALS_FILE)
        return df.set_index('user_type')['password'].to_dict()
    except Exception as e:
        print(f"Error reading credentials file: {e}")
        return {'owner': 'sshoney', 'employee': 'yellow'}

@app.route('/')
def index():
    if 'user_type' in session:
        return redirect(url_for('search'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        password = request.form.get('password', '').strip()
        credentials = get_credentials()
        
        if password == credentials.get('owner'):
            session['user_type'] = 'owner'
            return redirect(url_for('search'))
        elif password == credentials.get('employee'):
            session['user_type'] = 'employee'
            return redirect(url_for('search'))
        else:
            return render_template('login.html', error='Invalid password')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_type', None)
    return redirect(url_for('login'))

@app.route('/search', methods=['GET', 'POST'])
def search():
    if 'user_type' not in session:
        return redirect(url_for('login'))
    
    product = None
    if request.method == 'POST':
        identifier = request.form.get('identifier', '').strip()
        if identifier:
            product = get_product_info(identifier, session['user_type'])
    
    return render_template('search.html', 
                         user_type=session['user_type'],
                         product=product,
                         brand_name="S.S Plywood")

@app.route('/api/product/<identifier>')
def api_product(identifier):
    if 'user_type' not in session:
        return jsonify({'error': 'Not authenticated'}), 401
    
    product = get_product_info(identifier, session['user_type'])
    if product:
        return jsonify(product)
    return jsonify({'error': 'Product not found'}), 404


@app.route('/settings', methods=['GET', 'POST'])
def settings():
    if 'user_type' not in session or session['user_type'] != 'owner':
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        try:
            owner_password = request.form.get('owner_password', '').strip()
            employee_password = request.form.get('employee_password', '').strip()
            
            if not owner_password or not employee_password:
                return render_template('settings.html', 
                                     user_type=session['user_type'],
                                     error='Both passwords are required')
            
            # Update credentials file
            credentials = pd.DataFrame([
                {'user_type': 'owner', 'password': owner_password},
                {'user_type': 'employee', 'password': employee_password}
            ])
            credentials.to_excel(CREDENTIALS_FILE, index=False)
            
            return render_template('settings.html', 
                                 user_type=session['user_type'],
                                 success='Passwords updated successfully!')
        except Exception as e:
            return render_template('settings.html', 
                                 user_type=session['user_type'],
                                 error=f'Error updating passwords: {str(e)}')
    
    return render_template('settings.html', user_type=session['user_type'])

if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    app.run(debug=True, port=port)
