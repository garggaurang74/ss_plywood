# 🚀 Complete Heroku Deployment Guide

## What is Heroku?

Heroku is a cloud platform that lets you deploy your web app online in minutes. It's:
- ✅ **Easy to use** - No server management needed
- ✅ **Free tier available** - Great for testing
- ✅ **Automatic HTTPS** - Your app is secure
- ✅ **Auto-scaling** - Handles traffic spikes
- ✅ **One-click deployment** - Push code and it's live

---

## 📋 Prerequisites

Before starting, you need:
1. **Heroku Account** (free at https://www.heroku.com)
2. **Git installed** (check with `git --version`)
3. **Heroku CLI** (command-line tool)
4. **Your project files** (already ready!)

---

## 🎯 Step-by-Step Deployment

### **Step 1: Create Heroku Account**

1. Go to https://www.heroku.com
2. Click **"Sign up"**
3. Fill in your details
4. Verify your email
5. Create account

---

### **Step 2: Install Heroku CLI**

**On Mac:**
```bash
# Install using Homebrew
brew tap heroku/brew && brew install heroku

# Verify installation
heroku --version
```

Should show: `heroku/7.x.x` or similar

**On Windows:**
- Download from https://devcenter.heroku.com/articles/heroku-cli
- Run installer
- Restart terminal

**On Linux:**
```bash
curl https://cli-assets.heroku.com/install.sh | sh
```

---

### **Step 3: Login to Heroku**

```bash
heroku login
```

This will:
1. Open a browser window
2. Ask you to login
3. Return to terminal (logged in)

---

### **Step 4: Navigate to Your Project**

```bash
cd /Users/gauranggarg/CascadeProjects/windsurf-project-3/ss_plywood
```

---

### **Step 5: Initialize Git Repository**

```bash
# Check if git is already initialized
git status

# If not initialized, run:
git init
```

---

### **Step 6: Add All Files to Git**

```bash
git add .
```

This stages all your files for commit.

---

### **Step 7: Create Your First Commit**

```bash
git commit -m "Initial commit - S.S Plywood App"
```

This saves your files to git history.

---

### **Step 8: Create Heroku App**

```bash
heroku create ss-plywood-yourname
```

**Important:** Replace `yourname` with something unique!

Examples:
- `ss-plywood-gaurang`
- `ss-plywood-demo`
- `ss-plywood-2024`

**What this does:**
- Creates a new app on Heroku
- Sets up a remote git repository
- Assigns a unique URL

---

### **Step 9: Deploy Your App**

```bash
git push heroku main
```

**What happens:**
1. Uploads your code to Heroku
2. Installs dependencies from `requirements.txt`
3. Runs `Procfile` commands
4. Starts your app
5. Shows deployment logs

**Wait 2-3 minutes for deployment to complete.**

---

### **Step 10: Open Your App**

```bash
heroku open
```

This opens your app in the browser!

**Your app URL:** `https://ss-plywood-yourname.herokuapp.com`

---

## ✅ Verify Your App Works

1. **Login page should appear**
   - No demo text visible ✅
   - Beautiful gradient background ✅

2. **Test Owner Login**
   - Password: `sshoney`
   - Should see cost price ✅

3. **Test Employee Login**
   - Password: `yellow`
   - Should NOT see cost price ✅

4. **Test Search**
   - Search for: `SSP001`
   - Should find product ✅

5. **Test Mobile**
   - Open on phone
   - Should be responsive ✅

---

## 🔧 Common Issues & Solutions

### Issue 1: "Heroku command not found"
**Solution:**
```bash
# Reinstall Heroku CLI
brew tap heroku/brew && brew install heroku

# Or add to PATH
export PATH="/usr/local/heroku/bin:$PATH"
```

### Issue 2: "Not a git repository"
**Solution:**
```bash
git init
git add .
git commit -m "Initial commit"
```

### Issue 3: "App name already taken"
**Solution:**
```bash
# Use a different name
heroku create ss-plywood-unique-name
```

### Issue 4: "Deployment failed"
**Solution:**
```bash
# Check logs
heroku logs --tail

# Common causes:
# - Missing requirements.txt
# - Wrong Python version
# - Missing dependencies
```

### Issue 5: "App crashes after deployment"
**Solution:**
```bash
# View error logs
heroku logs --tail

# Restart app
heroku restart

# Check app status
heroku ps
```

---

## 📊 View App Logs

**Real-time logs:**
```bash
heroku logs --tail
```

**Last 50 lines:**
```bash
heroku logs -n 50
```

**Specific app:**
```bash
heroku logs -a ss-plywood-yourname
```

---

## 🔄 Update Your App

After making changes locally:

```bash
# 1. Make changes to your files
# 2. Add changes to git
git add .

# 3. Commit changes
git commit -m "Description of changes"

# 4. Deploy to Heroku
git push heroku main
```

Your app updates automatically!

---

## 🔐 Change Default Passwords

**Important:** Change these before sharing with team!

1. **Open your app** (from `heroku open`)
2. **Login as Owner** (password: `sshoney`)
3. **Click "Settings"**
4. **Enter new passwords**
5. **Click "Update Passwords"**

Now share the new employee password with your team.

---

## 📱 Share Your App

**Share this URL with your team:**
```
https://ss-plywood-yourname.herokuapp.com
```

**Share employee password:**
```
Password: [your-new-password]
```

---

## 💾 Data Persistence

**Current Setup:**
- Excel files stored on Heroku
- Data persists between restarts
- Good for small to medium apps

**For Production (Optional):**
Consider upgrading to a database:
- PostgreSQL (recommended)
- MySQL
- MongoDB

---

## 🆓 Free Tier Limits

Heroku free tier includes:
- ✅ 1 free app
- ✅ 512 MB RAM
- ✅ Automatic sleep after 30 mins of inactivity
- ✅ Free SSL/HTTPS
- ❌ No custom domain

**To keep app awake:**
- Upgrade to paid tier ($7/month)
- Or use external monitoring service

---

## 💰 Upgrade to Paid (Optional)

```bash
# View current dyno type
heroku ps

# Upgrade to paid
heroku dyno:type standard-1x

# Cost: $7/month (always-on)
```

---

## 🗑️ Delete Your App

If you want to remove your app:

```bash
heroku apps:destroy --app ss-plywood-yourname
```

**Warning:** This cannot be undone!

---

## 📈 Monitor Your App

```bash
# View app status
heroku ps

# View app info
heroku info

# View config variables
heroku config

# View recent deploys
heroku releases
```

---

## 🔗 Useful Heroku Commands

```bash
# Login/Logout
heroku login
heroku logout

# App management
heroku create app-name
heroku apps
heroku apps:destroy --app app-name

# Deployment
git push heroku main
heroku releases

# Logs
heroku logs --tail
heroku logs -n 50

# Restart
heroku restart

# Config
heroku config
heroku config:set KEY=value
heroku config:unset KEY

# Dyno management
heroku ps
heroku dyno:type standard-1x
```

---

## 🎓 What Happens During Deployment

1. **Code Upload** - Your files sent to Heroku
2. **Build** - Dependencies installed from `requirements.txt`
3. **Procfile** - Heroku reads `Procfile` to know how to start app
4. **Start** - App starts with `gunicorn app:app`
5. **Live** - App accessible at your URL

---

## 🚀 Next Steps

1. ✅ Create Heroku account
2. ✅ Install Heroku CLI
3. ✅ Follow steps 3-10 above
4. ✅ Test your app
5. ✅ Change default passwords
6. ✅ Share with team

---

## 📞 Help & Support

**Heroku Documentation:**
- https://devcenter.heroku.com/

**Common Issues:**
- https://devcenter.heroku.com/articles/troubleshooting-deploy-errors

**Status Page:**
- https://status.heroku.com/

---

## 🎉 Congratulations!

Your app is now live on the internet! 🌍

**Share your URL:**
```
https://ss-plywood-yourname.herokuapp.com
```

---

## 📋 Quick Reference

| Task | Command |
|------|---------|
| Login | `heroku login` |
| Create app | `heroku create app-name` |
| Deploy | `git push heroku main` |
| Open app | `heroku open` |
| View logs | `heroku logs --tail` |
| Restart | `heroku restart` |
| Update | `git push heroku main` |

---

**Status**: ✅ Ready to Deploy
**Last Updated**: November 23, 2025
