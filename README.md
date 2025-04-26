# Twitter Follower Bot ☠️

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Maintained](https://img.shields.io/badge/Maintained-yes-green.svg)
![Made by Seraph-666](https://img.shields.io/badge/Made%20by-Seraph--666-blueviolet.svg)

🚀 Automate following Twitter accounts directly from a list.
    
    > Twitter Follower Bot built using Selenium and undetected-chromedriver.




---

## Features
- Auto-follow users from a list of Twitter/X links.
- Skips users if already followed or error occurs.
- Removes followed users from the list automatically.
- Logs every follow or skip action.
- Randomized pauses to mimic human behavior.

## Demo
![2025-04-25 22-28-00 (online-video-cutter com)](https://github.com/user-attachments/assets/0e13341a-4b22-4b0e-9456-89d47ffcc0b1)


---

## Installation

```bash
git clone https://github.com/YOURUSERNAME/twitter-follower-bot.git
cd twitter-follower-bot
pip install -r requirements.txt
```
Usage
  1. Create a Create a **twitter_links.txt** file in the project folder.
      - Each line should be a full Twitter/X profile URL.

Example:
```bash
https://twitter.com/exampleuser
https://x.com/anotheruser
```
2. Adjust follo.py settings if needed:
  - CHROME_PROFILE_PATH
  - PROFILE_NAME
  - BATCH_LIMIT

3. Run the script:
```bash
python follo.py
```
## Requirements

Python 3.8+

Google Chrome installed

Chrome user profile path (pre-logged into Twitter)

## Notes

Uses undetected-chromedriver to reduce bot detection.

Chrome profile reuse avoids login prompts.


## Disclaimer

This project is for educational purposes only. Use at your own risk.



