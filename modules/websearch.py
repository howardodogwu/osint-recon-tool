import os
import requests
from dotenv import load_dotenv

load_dotenv()
SERPAPI_KEY = os.getenv("SERPAPI_KEY")

def serpapi_search(query):
    url = "https://serpapi.com/search"
    params = {
        "q": query,
        "engine": "google",
        "api_key": SERPAPI_KEY,
        "num": 5  # Number of results
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        results = response.json()
        # Extract top organic results
        return [
            {
                "title": r.get("title"),
                "link": r.get("link"),
                "snippet": r.get("snippet")
            }
            for r in results.get("organic_results", [])
        ]
    else:
        return [{"error": response.text}]