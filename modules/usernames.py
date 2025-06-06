import requests
from bs4 import BeautifulSoup

def check_usernames(username):
    """
    Search for the given username across multiple platforms.
    """
    results = {}
    platforms = {
        "GitHub": f"https://github.com/{username}",
        "Twitter": f"https://twitter.com/{username}",
        "Instagram": f"https://www.instagram.com/{username}"
    }

    for platform, url in platforms.items():
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                results[platform] = {"exists": True, "url": url}
            else:
                results[platform] = {"exists": False}
        except requests.RequestException:
            results[platform] = {"exists": False}
    
    return results
