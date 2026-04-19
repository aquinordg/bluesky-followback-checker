[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://python.org)
[![Windows](https://img.shields.io/badge/Windows-0078D6?logo=windows&logoColor=white)](https://github.com)
[![Linux](https://img.shields.io/badge/Linux-FCC624?logo=linux&logoColor=black)](https://github.com)
[![macOS](https://img.shields.io/badge/macOS-000000?logo=apple&logoColor=white)](https://github.com)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Bluesky](https://img.shields.io/badge/Bluesky-0085ff?logo=bluesky&logoColor=white)](https://bsky.app)

# 🦋 Bluesky Followback Checker

A Python script to identify who you follow on Bluesky but doesn't follow you back.

---

## ✨ Features

- ✅ Detects accounts you follow that don't follow you back
- ✅ Generates HTML report with clickable profile links
- ✅ Separates verified domain accounts from regular accounts
- ✅ Simple terminal interface with progress indicators
- ✅ No passwords are saved (secure)
- ✅ Cross-platform support (Windows, Linux, macOS)
- ✅ Automatic pagination for large followings

---

## 🚀 How to Use - Choose Your Option

### Option 1: For regular users (NO Python required) 🎯

**Windows only** - Download the ready-to-run executable:

1. Go to the [Releases page](https://github.com/aquinordg/bluesky-followback-checker/releases)
2. Download the `bluesky_followback.exe` file
3. **Double-click** the downloaded file
4. Follow the instructions in the terminal

> ⚠️ **Note**: Windows may show a security warning. Click "Run anyway" - it's safe!

**Quick download button:**

[![Download bluesky_followback.exe](https://img.shields.io/badge/Download_.exe_(Windows)-2ea44f?style=for-the-badge&logo=windows&logoColor=white)](https://github.com/aquinordg/bluesky-followback-checker/releases/latest/download/bluesky_followback.exe)

### Option 2: For users who prefer the source code 🐍

**Requires Python 3.7+ installed**

#### Quick installation:

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/bluesky-followback-checker.git
cd bluesky-followback-checker

# Install the dependency
pip install -r requirements.txt

# Run
python bluesky_followback.py
```

## 🚀 How to Use - Choose Your Option

### Option 1: For regular users (NO Python required) 🎯

**Windows only** - Download the ready-to-run executable:

1. Go to the [Releases page](https://github.com/YOUR_USERNAME/bluesky-followback-checker/releases)
2. Download the `bluesky_followback.exe` file
3. **Double-click** the downloaded file
4. Follow the instructions in the terminal

> ⚠️ **Note**: Windows may show a security warning. Click "Run anyway" - it's safe!

**Quick download button:**

[![Download bluesky_followback.exe](https://img.shields.io/badge/Download_.exe_(Windows)-2ea44f?style=for-the-badge&logo=windows&logoColor=white)](https://github.com/YOUR_USERNAME/bluesky-followback-checker/releases/latest/download/bluesky_followback.exe)

### Option 2: For users who prefer the source code 🐍

**Requires Python 3.7+ installed**

#### Quick installation:

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/bluesky-followback-checker.git
cd bluesky-followback-checker

# Install the dependency
pip install -r requirements.txt

# Run
python bluesky_followback.py
```

## Using automated scripts:

- **Windows**: Double-click `run.bat`
- **Mac/Linux**: Run `./run.sh` (use `chmod +x run.sh` first)

---

## 🔒 Security (IMPORTANT!)

### ⚠️ Always use an App Password!

For better security, **never use your main Bluesky password** with this tool. Instead:

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
- Passwords are entered via `getpass` (not visible on screen)
- Entire process runs locally on your computer
- Uses official Bluesky API (AT Protocol)

---

## 📊 How It Works

1. The script asks for your Bluesky **handle** (e.g., `username.bsky.social`) and **password** (use an App Password)
2. Authenticates with Bluesky's API using the AT Protocol
3. Fetches your complete "following" list (with automatic pagination)
4. Fetches your complete "followers" list
5. Compares both lists to find non-reciprocal follows
6. Generates an HTML report with statistics and clickable links
7. The report opens automatically in your browser

---

## 📸 Sample Generated Report

The HTML report includes:

- Total number of accounts not following back
- Complete list with direct links to Bluesky profiles
- Separation between regular accounts and verified domains
- Modern and responsive design with Bluesky's color scheme
- Clickable links that open in new tabs
- Timestamp of when the analysis was performed

---

## 📦 For Developers: Generating Your Own Executable

If you want to generate the executable yourself:

```bash
# Install PyInstaller
pip install pyinstaller

# Run the build script
python build_exe.py

# Or use PyInstaller directly
pyinstaller --onefile --console --name "bluesky_followback" --hidden-import=atproto bluesky_followback.py

# Or use the spec file
pyinstaller bluesky_followback.spec
```

The executable will be generated in the `dist/` folder

---

## 🖥️ Compatibility

| Operating System | Source Code (.py) | Executable |
|-------------------|-------------------|------------|
| Windows 10/11     | ✅ Yes            | ✅ Yes (download .exe) |
| macOS             | ✅ Yes            | ✅ Yes (build from source) |
| Linux             | ✅ Yes            | ✅ Yes (build from source) |

---

## ⚠️ Important Warnings

- **API Limits**: The script includes delays to respect Bluesky's rate limits
- **Large Accounts**: If you follow many people (+2000), the process may take a few minutes
- **Stable Connection**: Required to collect data
- **App Password Required**: Always use an App Password for security

---

## 🐛 Common Issues and Solutions

### "Windows protected your PC" when running the .exe

1. Click **"More info"**
2. Click **"Run anyway"**
3. This happens because the executable is new, but it's safe

### Login Error

**Solutions:**
- Verify your handle is correct (e.g., `username.bsky.social`)
- **Use an App Password** instead of your main password
- Check your internet connection
- Ensure Bluesky is operational

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

## 📄 License

Distributed under the MIT license. See `LICENSE` for more information.

---

## 🤝 Contributing

We welcome contributions! To contribute:

1. Fork this repository.
2. Create a new branch for your feature.
3. Submit a pull request with your changes.

For questions or information, feel free to reach out at: [aquinordga@gmail.com](mailto:aquinordga@gmail.com).

---

## 👨‍💻 Author

Developed by AQUINO, R. D. G. 
[![Lattes](https://github.com/aquinordg/custom_tools/blob/main/icons/icons8-plataforma-lattes-32.png)](http://lattes.cnpq.br/2373005809061037)
[![ORCID](https://github.com/aquinordg/custom_tools/blob/main/icons/icons8-orcid-32.png)](https://orcid.org/0000-0002-8486-8354)
[![Google Scholar](https://github.com/aquinordg/custom_tools/blob/main/icons/icons8-google-scholar-32.png)](https://scholar.google.com/citations?user=r5WsvKgAAAAJ&hl)

---

## 💬 Feedback

Feel free to open an issue or contact me for feedback or feature requests. Your input is highly appreciated!

---

## ⭐ Acknowledgments

- [AT Protocol](https://atproto.com/) - Bluesky's decentralized protocol
- [atproto Python Library](https://github.com/MarshalX/atproto) - Amazing library to interact with Bluesky
- [PyInstaller](https://pyinstaller.org/) - To generate standalone executables
- [Bluesky](https://bsky.app) - For creating an open social network

