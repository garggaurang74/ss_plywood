# S.S Plywood - Deployment Guide

This guide covers how to deploy the S.S Plywood application online.

## Option 1: Deploy to Heroku (Recommended for Beginners)

### Prerequisites
- Heroku account (free at https://www.heroku.com)
- Git installed
- Heroku CLI installed

### Steps

1. **Install Heroku CLI**
   ```bash
   brew tap heroku/brew && brew install heroku
   ```

2. **Login to Heroku**
   ```bash
   heroku login
   ```

3. **Create a Heroku App**
   ```bash
   cd /Users/gauranggarg/CascadeProjects/windsurf-project-3/ss_plywood
   heroku create your-app-name
   ```

4. **Initialize Git Repository** (if not already done)
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   ```

5. **Deploy to Heroku**
   ```bash
   git push heroku main
   ```

6. **Open Your App**
   ```bash
   heroku open
   ```

Your app will be available at: `https://your-app-name.herokuapp.com`

---

## Option 2: Deploy to Render (Free Alternative)

### Prerequisites
- Render account (free at https://render.com)
- GitHub account

### Steps

1. **Push code to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/yourusername/ss-plywood.git
   git push -u origin main
   ```

2. **Connect to Render**
   - Go to https://dashboard.render.com
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Select the repository
   - Configure:
     - **Name**: ss-plywood
     - **Environment**: Python 3
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `gunicorn app:app`

3. **Deploy**
   - Click "Create Web Service"
   - Wait for deployment to complete

Your app will be available at: `https://ss-plywood.onrender.com`

---

## Option 3: Deploy to PythonAnywhere

### Prerequisites
- PythonAnywhere account (free at https://www.pythonanywhere.com)

### Steps

1. **Create Account and Login**
   - Go to https://www.pythonanywhere.com
   - Sign up for free account

2. **Upload Files**
   - Go to "Files" tab
   - Create folder: `ss_plywood`
   - Upload all files from the project

3. **Create Web App**
   - Go to "Web" tab
   - Click "Add a new web app"
   - Choose "Python 3.9"
   - Choose "Flask"

4. **Configure WSGI File**
   - Edit the WSGI configuration file
   - Replace content with:
   ```python
   import sys
   path = '/home/yourusername/ss_plywood'
   if path not in sys.path:
       sys.path.append(path)
   from app import app as application
   ```

5. **Reload Web App**
   - Click "Reload" button

Your app will be available at: `https://yourusername.pythonanywhere.com`

---

## Option 4: Deploy to Railway

### Prerequisites
- Railway account (free at https://railway.app)
- GitHub account

### Steps

1. **Push to GitHub** (same as Render)

2. **Connect to Railway**
   - Go to https://railway.app
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Connect your repository

3. **Configure Environment**
   - Railway will auto-detect Flask
   - Set start command: `gunicorn app:app`

4. **Deploy**
   - Railway will automatically deploy

Your app will be available at the generated Railway URL

---

## Option 5: Deploy to Vercel (For Static Hosting)

Vercel doesn't support Python directly, but you can use Vercel's serverless functions.

---

## Local Deployment (For Testing)

To run locally on different ports:

```bash
# Default port 8000
python app.py

# Custom port
python app.py 3000
python app.py 5000
python app.py 9000
```

---

## Important Notes for Production

### 1. Change Secret Key
Before deploying, change the secret key in `app.py`:

```python
app.secret_key = 'your_secret_key_here'  # Change this!
```

Generate a secure key:
```python
import secrets
print(secrets.token_hex(32))
```

### 2. Update Passwords
Change default passwords in `credentials.xlsx`:
- Owner: Change from `sshoney`
- Employee: Change from `yellow`

### 3. Database Persistence
The app uses Excel files (`products.xlsx`, `credentials.xlsx`). For production:
- Consider using a real database (PostgreSQL, MySQL)
- Or use cloud storage (AWS S3, Google Cloud Storage)

### 4. Environment Variables
For sensitive data, use environment variables:

```python
import os
SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-key')
```

### 5. HTTPS
All deployment platforms above provide free HTTPS.

---

## Troubleshooting

### App Won't Start
- Check `requirements.txt` is in the project root
- Ensure all dependencies are listed
- Check logs: `heroku logs --tail` (for Heroku)

### File Upload Issues
- Excel files need to be writable
- Use cloud storage for production
- Consider using a database instead

### Port Issues
- Most platforms auto-assign ports
- Don't hardcode port numbers in production
- Use environment variables: `os.environ.get('PORT', 8000)`

---

## Recommended Deployment Platform

**For Beginners**: Heroku or Render (easiest setup)
**For Production**: Railway or Render (better performance)
**For Enterprise**: AWS, Google Cloud, or Azure

---

## Mobile-First Features

The application is fully responsive and optimized for:
- ✅ Mobile phones (320px and up)
- ✅ Tablets (768px and up)
- ✅ Desktops (1024px and up)
- ✅ Touch-friendly buttons and inputs
- ✅ Optimized for barcode scanners

---

## Support

For deployment issues:
1. Check platform-specific documentation
2. Review application logs
3. Ensure all files are uploaded
4. Verify environment variables are set
