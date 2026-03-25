import requests
import json
import pandas as pd
from collections import Counter
import re
from bs4 import BeautifulSoup
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
API_KEY = "YOUR_API_KEY_HERE" 
BASE_URL = "https://generativelanguage.googleapis.com/v1beta"

def get_best_model():
    """Finds a working model so we never get a 404 error again."""
    url = f"{BASE_URL}/models?key={API_KEY}"
    try:
        response = requests.get(url, verify=False)
        models = response.json().get('models', [])
        for m in models:
            if 'generateContent' in m['supportedGenerationMethods']:
                return m['name'].split('/')[-1]
    except: return "gemini-1.5-flash"
    return "gemini-1.5-flash"

def run_marketing_intelligence():
    print("[1/4] 🕷️  Scraping Competitor Headlines...")
    url = "https://quotes.toscrape.com/"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    titles = [t.text.lower() for t in soup.find_all('span', class_='text')]
    
    print("[2/4] 📊  Analyzing Keyword Trends...")
    all_words = re.findall(r'\w+', " ".join(titles))
    boring = ['the', 'is', 'to', 'and', 'of', 'in', 'that', 'it', 'with']
    filtered = [w for w in all_words if w not in boring and len(w) > 4]
    top_keyword = Counter(filtered).most_common(1)[0][0]
    print(f"-> Market Trend Identified: '{top_keyword}'")

    print("[3/4] 🤖  Asking AI for Localized Strategy...")
    model_name = get_best_model()
    ai_url = f"{BASE_URL}/models/{model_name}:generateContent?key={API_KEY}"
    
    prompt = f"""
    Act as a Senior Growth Engineer.
    Our trend analysis found the keyword: '{top_keyword}'.
    
    1. Write a funny Malayalam headline for a product using this keyword.
    2. Write a professional English ad description (50 words).
    3. Suggest a Python automation idea to scale this campaign.
    """
    
    payload = {"contents": [{"parts": [{"text": prompt}]}]}
    response = requests.post(ai_url, json=payload, verify=False)
    
    try:
        strategy = response.json()['candidates'][0]['content']['parts'][0]['text']
        
        print("[4/4] 📁  Saving Final Intelligence Report...")
        with open("automated_strategy_report.txt", "w", encoding="utf-8") as f:
            f.write(f"TECHNICAL MARKETING INTELLIGENCE REPORT\n")
            f.write(f"Trend Detected: {top_keyword.upper()}\n")
            f.write("-" * 40 + "\n")
            f.write(strategy)
        print("\n✅ PROJECT COMPLETE! Check 'automated_strategy_report.txt'")
    except:
        print("❌ AI Error: Check your API Key or Internet Connection.")

if __name__ == "__main__":
    run_marketing_intelligence()