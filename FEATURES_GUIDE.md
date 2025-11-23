# S.S Plywood - Features Guide

## 1. USER-SPECIFIC DATA DISPLAY

### Where It's Implemented:

#### **Backend (app.py)**
```python
# Line 70-84: Search route that passes user_type to template
@app.route('/search', methods=['GET', 'POST'])
def search():
    if 'user_type' not in session:
        return redirect(url_for('login'))
    
    product = None
    if request.method == 'POST':
        identifier = request.form.get('identifier', '').strip()
        if identifier:
            product = get_product_info(identifier)
    
    return render_template('search.html', 
                         user_type=session['user_type'],  # <-- USER TYPE PASSED HERE
                         product=product,
                         brand_name="S.S Plywood")
```

#### **Frontend (templates/search.html)**
```html
<!-- Lines 71-74: Conditional display based on user_type -->
{% if user_type == 'owner' %}
    <p><strong>Cost Price:</strong> ₹{{ product.price * 0.8 | round(2) }}</p>
    <p><strong>Profit Margin:</strong> 20%</p>
{% endif %}
```

### What Each User Sees:

**OWNER (password: sshoney)**
- ✅ Product Number
- ✅ Product Name
- ✅ Description
- ✅ **Cost Price** (80% of selling price)
- ✅ **Profit Margin** (20%)
- ✅ Selling Price
- ✅ Stock
- ✅ Barcode
- ✅ "Manage Products" button

**EMPLOYEE (password: yellow)**
- ✅ Product Number
- ✅ Product Name
- ✅ Description
- ✅ Selling Price ONLY
- ✅ Stock
- ✅ Barcode
- ❌ Cost Price (HIDDEN)
- ❌ Profit Margin (HIDDEN)
- ❌ "Manage Products" button (HIDDEN)

---

## 2. BARCODE SCANNING FUNCTIONALITY

### Where It's Implemented:

#### **Backend (app.py - Lines 29-43)**
```python
def get_product_info(identifier):
    try:
        df = pd.read_excel(EXCEL_FILE)
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
```

**This function:**
- Searches by product number first (case-insensitive)
- If not found, searches by barcode
- Returns product data as dictionary

#### **Frontend (templates/search.html - Lines 48-54)**
```html
<form method="POST" id="searchForm">
    <div class="input-group mb-3">
        <input type="text" class="form-control" id="identifier" name="identifier" 
               placeholder="Enter product number or scan barcode" autofocus>
        <button class="btn btn-primary" type="submit">Search</button>
    </div>
</form>
```

#### **JavaScript (templates/search.html - Lines 88-99)**
```javascript
<script>
    // Focus on the search input when page loads
    document.addEventListener('DOMContentLoaded', function() {
        document.getElementById('identifier').focus();
        
        // Auto-submit form when barcode scanner is used (assuming it adds an Enter key)
        document.getElementById('searchForm').addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                this.submit();
            }
        });
    });
</script>
```

### How Barcode Scanning Works:

1. **Input Field Always Focused** - When page loads, the search field is automatically focused
2. **Barcode Scanner Emulation** - Most barcode scanners work by:
   - Reading the barcode
   - Typing the barcode number into the focused field
   - Sending an Enter key
3. **Auto-Submit** - When Enter key is pressed, the form automatically submits
4. **Search Logic** - The backend searches for matching barcode in Excel file
5. **Display Results** - Product details are shown based on user type

### Testing Barcode Scanning:

**Test Barcodes in Demo Data:**
- SSP001: `8901234567001`
- SSP002: `8901234567002`
- SSP003: `8901234567003`
- SSP004: `8901234567004`
- SSP005: `8901234567005`
- SSP006: `8901234567006`

**To Test:**
1. Login to the app
2. Click on the search field
3. Type a barcode (e.g., `8901234567001`)
4. Press Enter
5. Product details will appear

---

## 3. USER AUTHENTICATION & SESSION MANAGEMENT

### Where It's Implemented:

#### **Backend (app.py - Lines 23-27)**
```python
# User credentials
USERS = {
    'owner': 'sshoney',
    'employee': 'yellow'
}
```

#### **Login Route (app.py - Lines 51-63)**
```python
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        password = request.form.get('password', '').strip()
        if password == USERS['owner']:
            session['user_type'] = 'owner'  # <-- STORES USER TYPE IN SESSION
            return redirect(url_for('search'))
        elif password == USERS['employee']:
            session['user_type'] = 'employee'  # <-- STORES USER TYPE IN SESSION
            return redirect(url_for('search'))
        else:
            return render_template('login.html', error='Invalid password')
    return render_template('login.html')
```

#### **Session Check (app.py - Lines 70-73)**
```python
@app.route('/search', methods=['GET', 'POST'])
def search():
    if 'user_type' not in session:  # <-- CHECKS IF USER IS LOGGED IN
        return redirect(url_for('login'))
```

---

## 4. DATA STORAGE

### Excel File Structure (products.xlsx)

The Excel file contains the following columns:

| Column | Type | Example |
|--------|------|---------|
| product_no | Text | SSP001 |
| barcode | Text | 8901234567001 |
| name | Text | Plywood 6mm Commercial |
| price | Number | 500 |
| stock | Number | 100 |
| description | Text | 6mm Commercial Grade Plywood |

### File Location:
```
/Users/gauranggarg/CascadeProjects/windsurf-project-3/ss_plywood/products.xlsx
```

### How Data is Read:
```python
# Line 31: Read Excel file
df = pd.read_excel(EXCEL_FILE)

# Line 33: Search by product number
product = df[df['product_no'].str.lower() == identifier.lower()]

# Line 36: Search by barcode
product = df[df['barcode'].astype(str) == identifier]
```

---

## 5. OWNER-ONLY FEATURES

### Manage Products Page

#### **Access Control (app.py - Lines 96-99)**
```python
@app.route('/manage', methods=['GET', 'POST'])
def manage():
    if 'user_type' not in session or session['user_type'] != 'owner':
        return redirect(url_for('login'))  # <-- ONLY OWNERS CAN ACCESS
```

#### **Frontend Check (templates/search.html - Lines 32-34)**
```html
{% if user_type == 'owner' %}
    <a href="{{ url_for('manage') }}" class="btn btn-outline-primary btn-sm ms-2">Manage Products</a>
{% endif %}
```

#### **Add/Edit Products (app.py - Lines 101-132)**
```python
if request.method == 'POST':
    try:
        product_no = request.form.get('product_no', '').strip()
        barcode = request.form.get('barcode', '').strip()
        name = request.form.get('name', '').strip()
        price = float(request.form.get('price', 0))
        stock = int(request.form.get('stock', 0))
        description = request.form.get('description', '').strip()
        
        df = pd.read_excel(EXCEL_FILE)
        
        # Check if product already exists
        if product_no in df['product_no'].values:
            # Update existing product
            df.loc[df['product_no'] == product_no, ['barcode', 'name', 'price', 'stock', 'description']] = [barcode, name, price, stock, description]
        else:
            # Add new product
            new_product = pd.DataFrame([{
                'product_no': product_no,
                'barcode': barcode,
                'name': name,
                'price': price,
                'stock': stock,
                'description': description
            }])
            df = pd.concat([df, new_product], ignore_index=True)
        
        df.to_excel(EXCEL_FILE, index=False)  # <-- SAVES TO EXCEL
```

---

## Summary

| Feature | Location | Purpose |
|---------|----------|---------|
| User-Specific Data | search.html (lines 71-74) | Show/hide owner-only fields |
| Barcode Scanning | app.py (lines 29-43) + search.html (lines 88-99) | Search by barcode or product number |
| Session Management | app.py (lines 51-63) | Store user type after login |
| Data Storage | products.xlsx | Excel file with all product data |
| Owner Features | app.py (lines 96-146) | Add/edit/manage products |
| Access Control | app.py (lines 70-73, 96-99) | Restrict pages by user type |
