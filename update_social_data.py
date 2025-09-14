import requests
from bs4 import BeautifulSoup
import json
import datetime

def fetch_instagram_followers(username="thegivingmovement"):
    url = f"https://socialblade.com/instagram/user/{username}"
    res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(res.text, "lxml")

    # Followers are inside "YouTubeUserTopInfo" blocks – fragile to site changes
    stats = soup.find_all("span", class_="YouTubeUserTopInfo")
    if stats and len(stats) > 1:
        followers = stats[1].text.strip().replace(",", "")
        return int(followers)
    return None

def fetch_tiktok_followers(username="thegivingmovement"):
    url = f"https://socialblade.com/tiktok/user/{username}"
    res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(res.text, "lxml")

    stats = soup.find_all("p", class_="YouTubeUserTopLight")
    if stats and len(stats) > 1:
        followers = stats[1].text.strip().replace(",", "")
        return int(followers)
    return None

def update_social_data():
    ig_followers = fetch_instagram_followers()
    tk_followers = fetch_tiktok_followers()

    data = {
        "last_updated": str(datetime.date.today()),
        "instagram": {
            "followers": ig_followers if ig_followers else 1230000,
            "posts": 1844   # update manually if needed
        },
        "tiktok": {
            "followers": tk_followers if tk_followers else 70100,
            "likes": 294600  # update manually if needed
        }
    }

    with open("social_data.json", "w") as f:
        json.dump(data, f, indent=4)

    print("✅ social_data.json updated:", data)

if __name__ == "__main__":
    update_social_data()
