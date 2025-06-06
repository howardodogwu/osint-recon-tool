import requests
from bs4 import BeautifulSoup
import socket

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

def domain_intelligence(domain):
    """
    Perform basic OSINT on a domain: resolve IP and get HTTP status.
    """
    results = {}
    try:
        ip = socket.gethostbyname(domain)
        results['ip_address'] = ip
    except Exception as e:
        results['ip_address'] = f"Error: {e}"

    try:
        response = requests.get(f"http://{domain}", timeout=5)
        results['http_status'] = response.status_code
    except Exception as e:
        results['http_status'] = f"Error: {e}"

    return results
