# S.S Plywood - Quick Start Guide

## 🚀 Get Started in 3 Minutes

### Step 1: Install Dependencies
```bash
cd /Users/gauranggarg/CascadeProjects/windsurf-project-3/ss_plywood
pip install -r requirements.txt
```

### Step 2: Run the Application
```bash
python app.py 8000
```

### Step 3: Open in Browser
Visit: **http://localhost:8000**

---

## 🔐 Login Credentials

| User Type | Password |
|-----------|----------|
| Owner | sshoney |
| Employee | yellow |

---

## 📱 Features

### For Employees
- 🔍 Search products by number or barcode
- 💵 View selling prices
- 📦 Check stock levels
- 🔖 Scan barcodes

### For Owners
- ✅ All employee features PLUS:
- 💰 View cost prices
- 📊 See profit margins
- ➕ Add/edit products
- 🔐 Change passwords
- 📋 Manage all product data

---

## 🎯 Key Features

### 1. **Separate Data Sheets**
- Owner sheet: Includes cost price and profit data
- Employee sheet: Only shows selling price and stock

### 2. **Barcode Scanning**
- Compatible with any barcode scanner
- Auto-submit on Enter key
- Search by product number or barcode

### 3. **Password Management**
- Owner can change both passwords
- Credentials stored in Excel file
- Secure session management

### 4. **Mobile-First Design**
- Works perfectly on phones
- Responsive on all screen sizes
- Touch-friendly interface
- Optimized for barcode scanners

### 5. **Product Management**
- Add new products
- Edit existing products
- View all products in table
- Auto-sync to Excel

---

## 📂 File Structure

```
ss_plywood/
├── app.py                    # Main application
├── requirements.txt          # Python dependencies
├── products.xlsx             # Product data (auto-created)
├── credentials.xlsx          # User passwords (auto-created)
├── Procfile                  # Heroku deployment
├── netlify.toml             # Netlify deployment
├── README.md                # Full documentation
├── DEPLOYMENT.md            # Deployment guide
├── FEATURES_GUIDE.md        # Feature details
├── QUICK_START.md           # This file
└── templates/
    ├── login.html           # Login page
    ├── search.html          # Product search
    ├── manage.html          # Product management
    └── settings.html        # Password settings
```

---

## 🧪 Test the App

### Test Data Available
6 sample products (SSP001-SSP006) with realistic data

### Test Barcodes
```
SSP001: 8901234567001
SSP002: 8901234567002
SSP003: 8901234567003
SSP004: 8901234567004
SSP005: 8901234567005
SSP006: 8901234567006
```

### How to Test
1. Login as Owner (password: `sshoney`)
2. Search for product: `SSP001`
3. Or scan barcode: `8901234567001`
4. View product details with cost price and profit
5. Click "Manage Products" to add/edit
6. Click "Settings" to change passwords

---

## 🌐 Deploy Online

### Easiest Option: Heroku
```bash
heroku login
heroku create your-app-name
git push heroku main
heroku open
```

### Alternative: Render
1. Push code to GitHub
2. Connect to Render
3. Deploy automatically

See `DEPLOYMENT.md` for detailed instructions.

---

## 🔧 Customize

### Change Brand Name
Edit `app.py` line 112:
```python
brand_name="Your Company Name"
```

### Change Colors
Edit CSS in template files (search for `#667eea`)

### Add More Products
1. Login as Owner
2. Go to "Manage Products"
3. Fill form and click "Save Product"

### Change Passwords
1. Login as Owner
2. Click "Settings"
3. Enter new passwords
4. Click "Update Passwords"

---

## 📊 Data Structure

### Products Sheet (Owner)
```
product_no | barcode | name | price | cost_price | stock | description
SSP001     | 890...  | ...  | 500   | 400        | 100   | ...
```

### Products Sheet (Employee)
```
product_no | barcode | name | price | stock | description
SSP001     | 890...  | ...  | 500   | 100   | ...
```

### Credentials Sheet
```
user_type | password
owner     | sshoney
employee  | yellow
```

---

## ⚡ Performance Tips

1. **Barcode Scanner Setup**
   - Configure scanner to send Enter key after barcode
   - Test with sample barcodes first

2. **Mobile Usage**
   - Use on mobile for best experience
   - Landscape mode for larger screens
   - Portrait mode for barcode scanning

3. **Data Management**
   - Regularly backup Excel files
   - Keep passwords secure
   - Update product data regularly

---

## 🆘 Troubleshooting

### App Won't Start
```bash
# Check Python version
python --version

# Reinstall dependencies
pip install -r requirements.txt --force-reinstall

# Try different port
python app.py 9000
```

### Barcode Scanner Not Working
- Check scanner is configured to send Enter key
- Test with manual typing first
- Ensure search field is focused

### Products Not Showing
- Check `products.xlsx` exists
- Verify Excel file has correct columns
- Restart the application

### Can't Login
- Check credentials in `credentials.xlsx`
- Default: owner=`sshoney`, employee=`yellow`
- Verify no extra spaces in password

---

## 📞 Support

For issues:
1. Check README.md for detailed documentation
2. Review FEATURES_GUIDE.md for feature details
3. See DEPLOYMENT.md for deployment help
4. Check application logs for errors

---

## 🎉 You're Ready!

The app is now running and ready to use. 

**Next Steps:**
1. Test with sample data
2. Add your own products
3. Deploy online (see DEPLOYMENT.md)
4. Share with your team

Enjoy! 🚀
