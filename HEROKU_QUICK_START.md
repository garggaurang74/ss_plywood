# 🚀 Heroku Deployment - Quick Start (5 Minutes)

## Copy-Paste Commands

Just copy and paste these commands in order!

---

## Step 1: Install Heroku CLI

```bash
brew tap heroku/brew && brew install heroku
```

Wait for installation to complete.

---

## Step 2: Verify Installation

```bash
heroku --version
```

Should show: `heroku/7.x.x` or similar

---

## Step 3: Login to Heroku

```bash
heroku login
```

A browser window will open. Login with your Heroku account.

---

## Step 4: Go to Your Project

```bash
cd /Users/gauranggarg/CascadeProjects/windsurf-project-3/ss_plywood
```

---

## Step 5: Initialize Git

```bash
git init
git add .
git commit -m "Initial commit - S.S Plywood App"
```

---

## Step 6: Create Heroku App

```bash
heroku create ss-plywood-yourname
```

**Replace `yourname` with something unique!**

Examples:
- `ss-plywood-gaurang`
- `ss-plywood-demo`
- `ss-plywood-2024`

---

## Step 7: Deploy Your App

```bash
git push heroku main
```

**Wait 2-3 minutes for deployment.**

You'll see lots of text - this is normal!

---

## Step 8: Open Your App

```bash
heroku open
```

Your app opens in browser! 🎉

---

## Step 9: Test Your App

1. **Login as Owner**
   - Password: `sshoney`
   - Should see cost price ✅

2. **Login as Employee**
   - Password: `yellow`
   - Should NOT see cost price ✅

3. **Search Product**
   - Search: `SSP001`
   - Should find product ✅

4. **Test Mobile**
   - Open on phone
   - Should be responsive ✅

---

## Step 10: Change Passwords

1. **Login as Owner** (password: `sshoney`)
2. **Click "Settings"**
3. **Enter new passwords**
4. **Click "Update Passwords"**
5. **Share new employee password with team**

---

## Your App is Live! 🎉

**Your URL:**
```
https://ss-plywood-yourname.herokuapp.com
```

**Share this with your team!**

---

## Update Your App Later

After making changes:

```bash
git add .
git commit -m "Description of changes"
git push heroku main
```

Your app updates automatically!

---

## View Logs (If Something Goes Wrong)

```bash
heroku logs --tail
```

This shows what's happening on your server.

---

## Common Issues

**"Heroku command not found"**
- Reinstall: `brew tap heroku/brew && brew install heroku`

**"App name already taken"**
- Use different name: `heroku create ss-plywood-unique-name`

**"Deployment failed"**
- Check logs: `heroku logs --tail`

---

## That's It!

Your app is now live on the internet! 🌍

**Next:** Share the URL with your team and change the passwords.

---

## Need Help?

Read the full guide: **HEROKU_GUIDE.md**

---

**Time to deploy: 5-10 minutes ⏱️**
