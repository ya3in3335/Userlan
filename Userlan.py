import os
import random
import string
import requests
import time
from colorama import Fore, Style, init

# Initialize colorama for Windows compatibility
init(autoreset=True)

# Clear screen function
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# Banner function
def show_banner():
    clear_screen()
    banner = f"""
{Fore.CYAN}██    ██ ██    ██ ███████ ██      ██████  █████  ███    ██ 
{Fore.CYAN}██    ██ ██    ██ ██      ██      ██      ██   ██ ████   ██ 
{Fore.CYAN}██    ██ ██    ██ █████   ██      ██      ███████ ██ ██  ██ 
{Fore.CYAN} ██  ██  ██    ██ ██      ██      ██      ██   ██ ██  ██ ██ 
{Fore.CYAN}  ████    ██████  ███████ ███████  ██████ ██   ██ ██   ████ 
{Fore.RED}       ░▒▓█ 𝙐𝙎𝙀𝙍𝙇𝘼𝙉 - 4-Letter Username Checker █▓▒░
{Fore.YELLOW}          🚀 Fast - ⚡ Powerful - 🎯 Accurate
{Fore.GREEN}          By: userlan | {Fore.MAGENTA}Telegram: https://t.me/hacker16_thsb
{Style.RESET_ALL}
"""
    print(banner)

# Generate a random 4-character username
def generate_username():
    chars = string.ascii_lowercase + string.digits
    return ''.join(random.choices(chars, k=4))

# Check if a username is available on Instagram
def check_username_availability(username):
    url = f"https://www.instagram.com/{username}/"
    response = requests.get(url)
    return response.status_code == 404  # 404 means the username is available

# Generate available usernames
def generate_valid_usernames(count, delay=1):
    valid_users = []
    
    while len(valid_users) < count:
        username = generate_username()
        if check_username_availability(username):
            valid_users.append(username)
            print(f"{Fore.GREEN}[✔] Available: {username}")
        else:
            print(f"{Fore.RED}[✘] Taken: {username}")
        
        time.sleep(delay)  # Prevent rate limiting
    
    return valid_users

# Main execution
if __name__ == "__main__":
    show_banner()
    
    num_users = int(input(f"{Fore.CYAN}How many usernames do you need? {Fore.YELLOW}"))
    valid_users = generate_valid_usernames(num_users)
    
    print(f"\n{Fore.GREEN}Available usernames:", valid_users)
