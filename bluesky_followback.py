#!/usr/bin/env python3
"""
Bluesky Followback Checker
Script para verificar quem não segue de volta no Bluesky
"""

from atproto import Client
from datetime import datetime
import webbrowser
import os
import sys
import getpass
import time

VERSION = "1.0.0"

def clear_screen():
    """Clear terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_banner():
    """Show initial banner"""
    clear_screen()
    print("="*60)
    print(f"            BLUESKY FOLLOWBACK CHECKER v{VERSION}")
    print("="*60)
    print()

def get_credentials():
    """Request user credentials"""
    show_banner()
    print(" PLEASE ENTER YOUR BLUESKY CREDENTIALS")
    print("="*50)
    
    handle = input("Enter your handle (ex: usuario.bsky.social): ").strip()
    if handle.startswith('@'):
        handle = handle[1:]
    
    print("\n Your password will not be saved and is used only for this session.")
    print("   Recommended: Use an App Password from Bluesky Settings")
    print("="*50)
    
    # Usando getpass para esconder a senha
    password = getpass.getpass("Enter your password (or app password): ")
    
    return handle, password

def get_all_follows(client):
    """Get all profiles you follow with pagination"""
    follows = []
    cursor = None
    
    while True:
        try:
            response = client.app.bsky.graph.get_follows({
                "actor": client.me.did,
                "limit": 100,
                "cursor": cursor
            })
            
            for follow in response.follows:
                follows.append({
                    'did': follow.did,
                    'handle': follow.handle,
                    'display_name': follow.display_name or '',
                    'avatar': follow.avatar if hasattr(follow, 'avatar') else None,
                    'is_verified': hasattr(follow, 'associated') and follow.associated and hasattr(follow.associated, 'did_handle') and follow.associated.did_handle if hasattr(follow, 'associated') else False
                })
            
            if not response.cursor:
                break
            cursor = response.cursor
            time.sleep(0.1)  # Pequena pausa para evitar rate limit
            
        except Exception as e:
            print(f"    Error fetching follows: {e}")
            break
    
    return follows

def get_all_followers(client):
    """Get all your followers with pagination"""
    followers = set()
    cursor = None
    
    while True:
        try:
            response = client.app.bsky.graph.get_followers({
                "actor": client.me.did,
                "limit": 100,
                "cursor": cursor
            })
            
            for follower in response.followers:
                followers.add(follower.did)
            
            if not response.cursor:
                break
            cursor = response.cursor
            time.sleep(0.1)  # Pequena pausa para evitar rate limit
            
        except Exception as e:
            print(f"    Error fetching followers: {e}")
            break
    
    return followers

def check_verified_domain(client, did):
    """Check if a profile has verified domain"""
    try:
        profile = client.app.bsky.actor.get_profile({"actor": did})
        # Verified if they have a domain in their handle (not .bsky.social)
        return '.' in profile.handle and not profile.handle.endswith('.bsky.social')
    except:
        return False

def save_html_report(all_users_dict, non_verified_list, verified_list, handle):
    """Save the list to an HTML file with clickable links"""
    filename = f'Bluesky_Followback_Report_{handle}_{datetime.now().strftime("%Y%m%d_%H%M%S")}.html'
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('<!DOCTYPE html>\n<html lang="en">\n<head>\n')
        f.write('<meta charset="UTF-8">\n')
        f.write('<meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
        f.write(f'<title>Bluesky Followback Report - @{handle}</title>\n')
        f.write("""
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif; background: linear-gradient(135deg, #0085ff 0%, #4c9aff 100%); min-height: 100vh; padding: 40px 20px; }
            .container { max-width: 1000px; margin: 0 auto; background: white; border-radius: 20px; box-shadow: 0 20px 60px rgba(0,0,0,0.3); overflow: hidden; }
            .header { background: linear-gradient(135deg, #0085ff 0%, #0055aa 100%); color: white; padding: 40px; text-align: center; }
            .header h1 { font-size: 2.5em; margin-bottom: 10px; }
            .header p { opacity: 0.9; font-size: 1.1em; }
            .content { padding: 40px; }
            .stats { background: #f8f9fa; border-radius: 15px; padding: 25px; margin-bottom: 30px; display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px; }
            .stat-card { text-align: center; }
            .stat-number { font-size: 2em; font-weight: bold; color: #0085ff; }
            .stat-label { color: #666; margin-top: 5px; }
            .section { margin-bottom: 40px; }
            .section h2 { color: #262626; border-bottom: 3px solid #0085ff; padding-bottom: 10px; margin-bottom: 20px; display: inline-block; }
            .user-list { display: grid; gap: 10px; }
            .user-item { background: #f8f9fa; padding: 12px 20px; border-radius: 10px; transition: all 0.3s ease; display: flex; align-items: center; }
            .user-item:hover { background: #e9ecef; transform: translateX(5px); }
            .user-number { font-weight: bold; color: #999; margin-right: 15px; min-width: 40px; }
            .username { font-weight: bold; color: #0085ff; text-decoration: none; font-size: 1.1em; }
            .username:hover { text-decoration: underline; }
            .fullname { color: #8e8e8e; margin-left: 10px; }
            .verified-badge { color: #0085ff; margin-left: 8px; font-weight: bold; }
            .footer { background: #f8f9fa; padding: 20px; text-align: center; color: #666; font-size: 0.9em; }
            @media (max-width: 768px) { .content { padding: 20px; } .header h1 { font-size: 1.8em; } }
        </style>
        """)
        f.write('</head>\n<body>\n')
        
        f.write('<div class="container">\n')
        f.write('<div class="header">\n')
        f.write(f'<h1>🦋 Bluesky Followback Report</h1>\n')
        f.write(f'<p>Analysis for <strong>@{handle}</strong></p>\n')
        f.write(f'<p>📅 {datetime.now().strftime("%d/%m/%Y at %H:%M:%S")}</p>\n')
        f.write('</div>\n')
        
        f.write('<div class="content">\n')
        f.write('<div class="stats">\n')
        f.write(f'<div class="stat-card"><div class="stat-number">{len(all_users_dict)}</div><div class="stat-label">Don\'t Follow Back</div></div>\n')
        f.write(f'<div class="stat-card"><div class="stat-number">{len(non_verified_list)}</div><div class="stat-label">Regular Accounts</div></div>\n')
        f.write(f'<div class="stat-card"><div class="stat-number">{len(verified_list)}</div><div class="stat-label">Verified Domains</div></div>\n')
        f.write('</div>\n')
        
        # Non-verified accounts
        if non_verified_list:
            f.write('<div class="section">\n<h2>👥 Regular Accounts</h2>\n<div class="user-list">\n')
            for i, (handle, info) in enumerate(non_verified_list, 1):
                f.write(f'<div class="user-item">')
                f.write(f'<span class="user-number">{i:3d}.</span>')
                f.write(f'<a href="https://bsky.app/profile/{handle}" target="_blank" class="username">@{handle}</a>')
                if info['display_name']:
                    f.write(f'<span class="fullname">- {info["display_name"]}</span>')
                f.write('</div>\n')
            f.write('</div>\n</div>\n')
        
        # Verified accounts
        if verified_list:
            f.write('<div class="section">\n<h2>✓ Verified Domains</h2>\n<div class="user-list">\n')
            start_num = len(non_verified_list) + 1
            for i, (handle, info) in enumerate(verified_list, start_num):
                f.write(f'<div class="user-item">')
                f.write(f'<span class="user-number">{i:3d}.</span>')
                f.write(f'<a href="https://bsky.app/profile/{handle}" target="_blank" class="username">@{handle}</a>')
                f.write('<span class="verified-badge"> ✓ VERIFIED DOMAIN</span>')
                if info['display_name']:
                    f.write(f'<span class="fullname">- {info["display_name"]}</span>')
                f.write('</div>\n')
            f.write('</div>\n</div>\n')
        
        f.write('</div>\n')
        f.write('<div class="footer">\n')
        f.write('<p>Generated by Bluesky Followback Checker | Report opens profiles in new tabs</p>\n')
        f.write('</div>\n')
        f.write('</div>\n')
        f.write('</body>\n</html>')
    
    return filename

def main():
    """Main function"""
    try:
        handle, password = get_credentials()
        
        print("\n Logging into Bluesky...")
        
        try:
            client = Client()
            client.login(handle, password)
            print(" Login successful!")
        except Exception as e:
            print(f" Login error: {e}")
            print("\n Tips:")
            print("   - Check your handle and password")
            print("   - Use an App Password from Bluesky Settings")
            print("   - Go to Settings > App Passwords to create one")
            input("\nPress Enter to exit...")
            return
        
        print(f"\n Loading profile data...")
        
        # Collect data
        print("\n Searching for people you follow...")
        print("    This may take a few minutes...")
        following = {}
        follows_list = get_all_follows(client)
        
        for follow in follows_list:
            following[follow['did']] = {
                'handle': follow['handle'],
                'display_name': follow['display_name'],
                'is_verified': follow['is_verified']
            }
            if len(following) % 50 == 0:
                print(f"    Found {len(following)} profiles so far...")
        print(f" Found {len(following)} profiles you follow")
        
        print("\n Searching for your followers...")
        print("    This may take a few minutes...")
        followers_set = get_all_followers(client)
        print(f" Found {len(followers_set)} followers")
        
        # People you follow but who don't follow you back
        non_followers = {did: info for did, info in following.items() if did not in followers_set}
        
        # Check for verified domains
        print("\n Checking for verified domains...")
        verified_users = []
        non_verified_users = []
        
        for did, info in non_followers.items():
            # Check if handle has custom domain (verified)
            if '.' in info['handle'] and not info['handle'].endswith('.bsky.social'):
                verified_users.append((info['handle'], info))
            else:
                non_verified_users.append((info['handle'], info))
        
        # Sort alphabetically
        non_verified_sorted = sorted(non_verified_users, key=lambda x: x[0].lower())
        verified_sorted = sorted(verified_users, key=lambda x: x[0].lower())
        
        print(f"\n Analysis completed!")
        print(f"   - Total profiles you follow: {len(following)}")
        print(f"   - Total followers: {len(followers_set)}")
        print(f"   - Profiles that don't follow you back: {len(non_followers)}")
        print(f"     - Regular accounts: {len(non_verified_sorted)}")
        print(f"     - Verified domains: {len(verified_sorted)}")
        
        # Generate report
        html_filename = save_html_report(
            non_followers,
            non_verified_sorted,
            verified_sorted,
            handle
        )
        
        # Open report in browser
        try:
            webbrowser.open(f'file://{os.path.abspath(html_filename)}')
            print(f"\n Report opened automatically in your browser!")
            print(f" File saved as: {html_filename}")
        except Exception:
            print(f"\n Report saved as: {html_filename}")
            print(" You can open it manually in any web browser")
        
        print("\n Analysis completed successfully!")
        print(" Tip: In the HTML report, click on any username to open their Bluesky profile")
        
        input("\n Press Enter to exit...")
        
    except KeyboardInterrupt:
        print("\n\n Operation cancelled by user.")
    except Exception as e:
        print(f"\n Unexpected error: {e}")
        input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()