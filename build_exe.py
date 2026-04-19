#!/usr/bin/env python3
"""
Script to generate the .exe executable for Bluesky Followback Checker
Run: python build_exe.py
"""

import os
import sys
import shutil
import subprocess
import glob

def check_pyinstaller():
    """Check if PyInstaller is installed"""
    try:
        import PyInstaller
        print(" PyInstaller found")
        return True
    except ImportError:
        print(" PyInstaller not installed")
        print("\n Installing PyInstaller...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
        print(" PyInstaller installed successfully!")
        return True

def clean_old_build():
    """Clean previous builds"""
    print("\n Cleaning previous builds...")
    
    folders_to_remove = ['build', 'dist', '__pycache__']
    for folder in folders_to_remove:
        if os.path.exists(folder):
            shutil.rmtree(folder)
            print(f"   Removed: {folder}")
    
    files_to_remove = glob.glob('*.spec')
    for file in files_to_remove:
        os.remove(file)
        print(f"   Removed: {file}")

def build_executable():
    """Generate the executable"""
    print("\n Generating executable...")
    print("   This may take a few minutes...")
    
    # PyInstaller command for Bluesky
    cmd = [
        "pyinstaller",
        "--onefile",           # Single file
        "--console",           # Terminal window
        "--name", "bluesky_followback",
        "--clean",             # Clean cache
        "--noconfirm",         # Don't ask for confirmations
        "--hidden-import", "atproto",  # Main Bluesky library
        "--hidden-import", "getpass",   # For secure password input
        "--hidden-import", "webbrowser", # To open the report
        "--hidden-import", "time",       # For API delays
        "bluesky_followback.py"
    ]
    
    try:
        subprocess.run(cmd, check=True, capture_output=False)
        print("\n Executable generated successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"\n Error generating executable: {e}")
        return False

def show_result():
    """Show where the executable was generated"""
    exe_path = os.path.join("dist", "bluesky_followback.exe")
    
    if os.path.exists(exe_path):
        size = os.path.getsize(exe_path) / (1024 * 1024)  # Size in MB
        print("\n" + "="*60)
        print(" BUILD COMPLETED SUCCESSFULLY! ")
        print("="*60)
        print(f"\n Executable generated at: {exe_path}")
        print(f" Size: {size:.2f} MB")
        print("\n To distribute:")
        print("   1. Copy the .exe file anywhere you want")
        print("   2. User just needs to double-click it!")
        print("   3. Make sure the user has a Bluesky account")
        print("\n Tip: Add this .exe to your GitHub releases")
        print("\n Security note: Recommend using an App Password from Bluesky")
        print("   (Settings > App Passwords)")
    else:
        print("\n Error: Executable not found!")

def main():
    """Main function"""
    print("="*60)
    print("    EXECUTABLE BUILDER - BLUESKY FOLLOWBACK")
    print("="*60)
    print("\n This build is exclusively for Bluesky")
    print("   (No relation to Instagram or other networks)")
    print()
    
    # Create auxiliary files
    create_requirements()
    create_version_info()
    create_bat_file()
    create_readme_txt()
    
    # Check PyInstaller
    if not check_pyinstaller():
        print(" Cannot continue without PyInstaller")
        sys.exit(1)
    
    # Clean old builds
    clean_old_build()
    
    # Generate executable
    if build_executable():
        show_result()
        print("\n Done! Now you can distribute the executable!")
        print("\n The following files were created:")
        print("   - dist/bluesky_followback.exe (main executable)")
        print("   - Run_Bluesky_Checker.bat (shortcut to run)")
        print("   - README.txt (user instructions)")
        print("   - requirements.txt (dependencies)")
    else:
        print("\n Failed to generate executable")
        sys.exit(1)

if __name__ == "__main__":
    main()