from flask import Flask, render_template, request, redirect, url_for, send_file
from modules.usernames import check_usernames
from modules.domains import domain_intelligence
from modules.emails import email_lookup
from reports.report_generator import generate_report
from modules.websearch import serpapi_search
import os
import subprocess
import whois
import requests
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

def sherlock_search(username):
    result = subprocess.run(['sherlock', username, '--print-found'], capture_output=True, text=True)
    return result.stdout

def whois_lookup(domain):
    try:
        w = whois.whois(domain)
        return w
    except Exception as e:
        return {"error": str(e)}

def google_search(query, api_key):
    params = {
        "q": query,
        "api_key": api_key,
        "engine": "google"
    }
    response = requests.get("https://serpapi.com/search", params=params)
    return response.json()

# Home Page with Input Form
@app.route("/", methods=["GET", "POST"])
def index():
    results = {"username": {}, "domain": {}, "email": {}}
    if request.method == "POST":
        user_input = request.form.get("username")
        # Run all modules with the same input
        results["username"] = check_usernames(user_input)
        results["domain"] = domain_intelligence(user_input)
        results["email"] = email_lookup(user_input)
        results["web_search"] = serpapi_search(user_input)
        return render_template("report_template.html", data=results, now=datetime.now().strftime("%Y-%m-%d %H:%M"))
    return render_template("index.html")

# Results Page
@app.route("/results")
def results():
    # Load results for display
    json_path = os.path.join("reports", "output.json")
    return render_template("results.html", json_file=json_path)

# Download Route
@app.route("/download/<format>")
def download(format):
    path = f"reports/output.{format}"
    return send_file(path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
