# 🦋 Bluesky Followback Checker

## 🎯 About
Tool to identify who you follow on Bluesky but doesn't follow you back.

## ✨ Features
- ✅ Detects accounts you follow that don't follow you back
- ✅ Generates HTML report with clickable profile links
- ✅ Separates verified domain accounts from regular accounts
- ✅ Simple terminal interface with progress indicators
- ✅ No passwords are saved (secure)
- ✅ Cross-platform support (Windows, Linux, macOS)
- ✅ Automatic pagination for large followings

## 🚀 How to Use

### Windows Users (Executable)
1. Download the `bluesky_followback.exe` file
2. Double-click to run it
3. Enter your Bluesky handle (e.g., `username.bsky.social`)
4. Enter your **App Password** (recommended for security)
5. Wait for the analysis (may take a few minutes)
6. The HTML report will open automatically in your browser

### Linux/macOS Users (Source Code)
```bash
git clone https://github.com/aquinordg/bluesky-followback-checker.git
cd bluesky-followback-checker
pip install -r requirements.txt
python bluesky_followback.py
```

## 🔒 Security (IMPORTANT!)

### ⚠️ Always use an App Password!

**Never use your main Bluesky password** with this tool. Instead:

1. Go to Bluesky Settings → **App Passwords**
2. Click "Add App Password"
3. Name it (e.g., "Followback Checker")
4. Copy the generated password
5. Use this password when the script asks for it

**Why?**
- You can revoke the app password anytime
- Limited scope and permissions
- Your main password remains secure

### Security Features

- **No credentials are saved** to files
- Passwords are entered via terminal (not visible on screen)
- Entire process runs locally on your computer
- Uses official Bluesky API (AT Protocol)

---

## 📊 Sample Generated Report

The HTML report includes:

- Total number of accounts not following back
- Complete list with direct links to Bluesky profiles
- Separation between regular accounts and verified domains
- Modern and responsive design with Bluesky's color scheme
- Clickable links that open in new tabs
- Timestamp of analysis

---

## ⚠️ Important Warnings

- **API Limits**: The script includes delays to respect Bluesky's rate limits
- **Large Accounts**: If you follow many people (+2000), the process may take a few minutes
- **Stable Connection**: Required to collect data
- **App Password Required**: Always use an App Password for security

---

## 🐛 Troubleshooting

### "Windows protected your PC" when running the .exe

1. Click **"More info"**
2. Click **"Run anyway"**
3. This is normal for new programs, it's safe

### Login Error

**Solutions:**
- Verify your handle is correct (e.g., `username.bsky.social`)
- **Use an App Password** instead of your main password
- Check your internet connection
- Ensure Bluesky is operational (check status.bsky.app)

### Script is taking too long

- Normal for accounts with many follows (5-10 minutes for 5000+)
- The script adds delays to respect API limits
- Your internet connection speed affects fetch times

### "No module named 'atproto'" error

```bash
pip install atproto
```

### HTML report doesn't open automatically

- Look for a file named `Bluesky_Followback_Report_*.html`
- Open it manually in your browser

---

## 📋 Requirements

- **Windows**: Windows 10 or 11 (for the executable)
- **Linux/macOS**: Python 3.7+ (to run the source code)
- **All platforms**: Bluesky account and internet connection

---

## 🔄 What's New in This Version

### Version 1.0.0

- Initial release
- Basic followback checking functionality
- HTML report generation
- Verified domain detection
- Cross-platform support
- GitHub Actions automation

---

## 🗺️ Roadmap

- [ ] Option to unfollow non-reciprocal accounts
- [ ] Export results to CSV/JSON
- [ ] Graphical user interface (GUI)
- [ ] Schedule automatic checks
- [ ] Compare with previous reports

---

## 🤝 Contributing

Contributions are welcome!

- Report bugs via GitHub Issues
- Submit pull requests for improvements
- Suggest new features

---

## 📄 License

MIT License - See the LICENSE file in the repository

---

## 🙏 Support

- 📧 Email: [aquinordga@gmail.com](mailto:aquinordga@gmail.com)
- 🐙 GitHub Issues: [Create an issue](https://github.com/aquinordg/bluesky-followback-checker/issues)
- 🦋 Bluesky: [@aquino.bsky.social](https://bsky.app/profile/@aquino.bsky.social)

---

**Thank you for using Bluesky Followback Checker!** 🦋