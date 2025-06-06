import requests

HIBP_API_KEY = "your_hibp_api_key_here"
HUNTER_API_KEY = "your_hunter_api_key_here"

def email_lookup(email):
    """
    Perform email investigation using HaveIBeenPwned and Hunter.io.
    """
    results = {}

    # HaveIBeenPwned - Breach Check
    try:
        hibp_headers = {"hibp-api-key": HIBP_API_KEY}
        hibp_url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
        response = requests.get(hibp_url, headers=hibp_headers, timeout=5)
        if response.status_code == 200:
            results['breaches'] = response.json()
        elif response.status_code == 404:
            results['breaches'] = "No breaches found."
        else:
            results['breaches'] = "Error occurred."
    except Exception as e:
        results['breaches'] = {"error": str(e)}

    # Hunter.io Lookup
    try:
        hunter_url = f"https://api.hunter.io/v2/email-verifier?email={email}&api_key={HUNTER_API_KEY}"
        response = requests.get(hunter_url, timeout=5)
        results['hunter'] = response.json()
    except Exception as e:
        results['hunter'] = {"error": str(e)}

    return results
