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
    
    # Check if employees are disabled
    disable_file = 'employee_disabled.txt'
    if session['user_type'] == 'employee' and os.path.exists(disable_file):
        session.pop('user_type', None)
        return render_template('login.html', error='Employee access is currently disabled by owner. Please contact your manager.')
    
    # Check if there's a logout timestamp (force logout all employees)
    logout_timestamp_file = 'employee_logout_timestamp.txt'
    if session['user_type'] == 'employee' and os.path.exists(logout_timestamp_file):
        session.pop('user_type', None)
        return render_template('login.html', error='Your session has been terminated by the owner. Please login again.')
    
    product = None
    search_performed = False
    searched_identifier = ''
    
    if request.method == 'POST':
        identifier = request.form.get('identifier', '').strip()
        if identifier:
            search_performed = True
            searched_identifier = identifier
            product = get_product_info(identifier, session['user_type'])
    
    return render_template('search.html', 
                         user_type=session['user_type'],
                         product=product,
                         search_performed=search_performed,
                         searched_identifier=searched_identifier,
                         brand_name="S.S Plywood")

@app.route('/api/product/<identifier>')
def api_product(identifier):
    if 'user_type' not in session:
        return jsonify({'error': 'Not authenticated'}), 401
    
    # Check if employees are disabled or logged out
    disable_file = 'employee_disabled.txt'
    logout_timestamp_file = 'employee_logout_timestamp.txt'
    if session['user_type'] == 'employee' and (os.path.exists(disable_file) or os.path.exists(logout_timestamp_file)):
        session.pop('user_type', None)
        return jsonify({'error': 'Access denied. Employee access has been disabled.'}), 403
    
    product = get_product_info(identifier, session['user_type'])
    if product:
        return jsonify(product)
    return jsonify({'error': 'Product not found'}), 404


@app.route('/logout-employee', methods=['POST'])
def logout_employee():
    if 'user_type' not in session or session['user_type'] != 'owner':
        return jsonify({'error': 'Unauthorized'}), 401
    
    try:
        # Create a file to disable employee access
        disable_file = 'employee_disabled.txt'
        with open(disable_file, 'w') as f:
            f.write('disabled')
        
        # Create a logout timestamp file to force all employee sessions to logout
        logout_timestamp_file = 'employee_logout_timestamp.txt'
        import time
        with open(logout_timestamp_file, 'w') as f:
            f.write(str(time.time()))
        
        return jsonify({'success': True, 'message': 'All employees have been logged out and access disabled'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/enable-employee', methods=['POST'])
def enable_employee():
    if 'user_type' not in session or session['user_type'] != 'owner':
        return jsonify({'error': 'Unauthorized'}), 401
    
    try:
        # Remove the disable file to re-enable access
        disable_file = 'employee_disabled.txt'
        if os.path.exists(disable_file):
            os.remove(disable_file)
        
        # Also remove the logout timestamp file
        logout_timestamp_file = 'employee_logout_timestamp.txt'
        if os.path.exists(logout_timestamp_file):
            os.remove(logout_timestamp_file)
        
        return jsonify({'success': True, 'message': 'Employee access has been re-enabled'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/manage', methods=['GET'])
def manage():
    if 'user_type' not in session or session['user_type'] != 'owner':
        return redirect(url_for('login'))
    
    try:
        # Only owner can see manage page - owner sheet only
        df = pd.read_excel(EXCEL_FILE, sheet_name='owner')
        products = df.to_dict('records')
    except:
        products = []
    
    return render_template('manage.html', 
                         user_type=session['user_type'],
                         products=products)


@app.route('/settings', methods=['GET', 'POST'])
def settings():
    if 'user_type' not in session or session['user_type'] != 'owner':
        return redirect(url_for('login'))
    
    # Get current passwords
    current_passwords = {'owner': '', 'employee': ''}
    try:
        creds_df = pd.read_excel(CREDENTIALS_FILE)
        for _, row in creds_df.iterrows():
            if row['user_type'] == 'owner':
                current_passwords['owner'] = row['password']
            elif row['user_type'] == 'employee':
                current_passwords['employee'] = row['password']
    except:
        pass
    
    if request.method == 'POST':
        try:
            owner_password = request.form.get('owner_password', '').strip()
            employee_password = request.form.get('employee_password', '').strip()
            
            if not owner_password or not employee_password:
                return render_template('settings.html', 
                                     user_type=session['user_type'],
                                     current_owner_password=current_passwords['owner'],
                                     current_employee_password=current_passwords['employee'],
                                     error='Both passwords are required')
            
            # Update credentials file
            credentials = pd.DataFrame([
                {'user_type': 'owner', 'password': owner_password},
                {'user_type': 'employee', 'password': employee_password}
            ])
            credentials.to_excel(CREDENTIALS_FILE, index=False)
            
            return render_template('settings.html', 
                                 user_type=session['user_type'],
                                 current_owner_password=owner_password,
                                 current_employee_password=employee_password,
                                 success='Passwords updated successfully!')
        except Exception as e:
            return render_template('settings.html', 
                                 user_type=session['user_type'],
                                 current_owner_password=current_passwords['owner'],
                                 current_employee_password=current_passwords['employee'],
                                 error=f'Error updating passwords: {str(e)}')
    
    return render_template('settings.html', 
                         user_type=session['user_type'],
                         current_owner_password=current_passwords['owner'],
                         current_employee_password=current_passwords['employee'])

if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    app.run(debug=True, port=port)
