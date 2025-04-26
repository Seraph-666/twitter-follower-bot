import time
import re
import random
import os
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from colorama import Fore, Style, init

init(autoreset=True)  # Auto reset color after print

# === BANNER ===
banner = """ 
▒██   ██▒     █████▒█████  ██▓    ██▓    ▒█████  █     █▓█████ ██▀███  
▒▒ █ █ ▒░   ▓██   ▒██▒  ██▓██▒   ▓██▒   ▒██▒  ██▓█░ █ ░█▓█   ▀▓██ ▒ ██▒
░░  █   ░   ▒████ ▒██░  ██▒██░   ▒██░   ▒██░  ██▒█░ █ ░█▒███  ▓██ ░▄█ ▒
 ░ █ █ ▒    ░▓█▒  ▒██   ██▒██░   ▒██░   ▒██   ██░█░ █ ░█▒▓█  ▄▒██▀▀█▄  
▒██▒ ▒██▒   ░▒█░  ░ ████▓▒░██████░██████░ ████▓▒░░██▒██▓░▒████░██▓ ▒██▒
▒▒ ░ ░▓ ░    ▒ ░  ░ ▒░▒░▒░░ ▒░▓  ░ ▒░▓  ░ ▒░▒░▒░░ ▓░▒ ▒ ░░ ▒░ ░ ▒▓ ░▒▓░
░░   ░▒ ░    ░      ░ ▒ ▒░░ ░ ▒  ░ ░ ▒  ░ ░ ▒ ▒░  ▒ ░ ░  ░ ░  ░ ░▒ ░ ▒░
 ░    ░      ░ ░  ░ ░ ░ ▒   ░ ░    ░ ░  ░ ░ ░ ▒   ░   ░    ░    ░░   ░ 
 ░    ░               ░ ░     ░  ░   ░  ░   ░ ░     ░      ░  ░  ░     
                        
                        https://t.me/Bytebl33d3r                                           
"""

print(Fore.GREEN + banner + Style.RESET_ALL)

# === CONFIG ===
INPUT_FILE = "twitter_links.txt"
CHROME_PROFILE_PATH = "C:/Users/admin1/AppData/Local/Google/Chrome/User Data"
PROFILE_NAME = "Default"
LOG_FILE = "follow_log.txt"
BATCH_LIMIT = 50  # Stop after this many successful follows
SHORT_WAIT = 1.5  # Short timeout in seconds

# === SETUP CHROME ===
options = uc.ChromeOptions()
options.add_argument(f"--user-data-dir={CHROME_PROFILE_PATH}")
options.add_argument(f"--profile-directory={PROFILE_NAME}")
driver = uc.Chrome(options=options)

# === LOAD USERNAMES FROM FILE ===
def extract_usernames(filename):
    usernames = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            match = re.search(r"(?:twitter\.com|x\.com)/([A-Za-z0-9_]{1,15})", line.strip())
            if match:
                usernames.append((match.group(1), line.strip()))
    return usernames

# === REMOVE FOLLOWED USERS FROM FILE ===
def remove_followed_from_file(followed_lines):
    if not followed_lines:
        return
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        all_lines = f.readlines()
    remaining_lines = [line for line in all_lines if line.strip() not in followed_lines]
    with open(INPUT_FILE, "w", encoding="utf-8") as f:
        f.writelines(remaining_lines)

# === FOLLOW FUNCTION ===
def follow_user(username):
    url = f"https://twitter.com/{username}"
    driver.get(url)

    try:
        follow_btn = WebDriverWait(driver, SHORT_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(@data-testid, "-follow")]'))
        )
        driver.execute_script("arguments[0].click();", follow_btn)
        print(f"✅ Followed: {username}")
        return True
    except Exception:
        print(f"⏩ Skipped: {username}")
        return False

# === MAIN SCRIPT ===
usernames = extract_usernames(INPUT_FILE)
print(f"👥 Loaded {len(usernames)} accounts.")

successful_follows = 0
followed_lines_to_remove = []

start_time = time.time()

for username, original_line in usernames:
    if follow_user(username):
        successful_follows += 1
        followed_lines_to_remove.append(original_line)
        with open(LOG_FILE, "a", encoding="utf-8") as log:
            log.write(f"{username} ✅ Followed\n")
    else:
        with open(LOG_FILE, "a", encoding="utf-8") as log:
            log.write(f"{username} ⏩ Skipped\n")

    if successful_follows > 0 and successful_follows % BATCH_LIMIT == 0:
        print(f"🛑 Hit {BATCH_LIMIT} successful follows. Stopping.")
        break

    # way faster random pause
    time.sleep(random.uniform(1.0, 2.5))

remove_followed_from_file(followed_lines_to_remove)

end_time = time.time()
print(f"✅ Done. Total time: {round(end_time - start_time, 2)} seconds.")
driver.quit()
