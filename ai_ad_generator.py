import requests
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
API_KEY = "YOUR_API_KEY_HERE"
BASE_URL = "https://generativelanguage.googleapis.com/v1beta"
winning_product = "High-Performance Mechanical Keyboard for Coders"
target_audience = "Software Engineers in the UK"
prompt_text = f"Act as a Senior Copywriter. Write 3 Meta Ad headlines for '{winning_product}'."
def get_working_model(api_key):
    """Dynamically finds the best working AI model for this account."""
    print("[System] 🔍 Scanning for available AI models...")
    list_url = f"{BASE_URL}/models?key={api_key}"    
    try:
        response = requests.get(list_url, verify=False)
        models_data = response.json()        
        for model in models_data.get('models', []):
            model_name = model['name'].split('/')[-1]
            if 'generateContent' in model['supportedGenerationMethods']:
                test_url = f"{BASE_URL}/models/{model_name}:generateContent?key={api_key}"
                test_payload = {"contents": [{"parts": [{"text": "hi"}]}]}
                res = requests.post(test_url, json=test_payload, verify=False)
                if res.status_code == 200:
                    print(f"✅ Found Working Model: {model_name}")
                    return model_name
    except Exception as e:
        print(f"❌ Discovery Error: {e}")
    return None
def generate_marketing_content(api_key, model_name):
    """Uses the discovered model to generate professional ad copy."""
    print(f"[System] 🚀 Generating content using {model_name}...")
    url = f"{BASE_URL}/models/{model_name}:generateContent?key={api_key}"    
    payload = {"contents": [{"parts": [{"text": prompt_text}]}]}    
    try:
        response = requests.post(url, json=payload, verify=False)
        result = response.json()
        ai_text = result['candidates'][0]['content']['parts'][0]['text']        
        print("\n--- AI GENERATED CONTENT ---")
        print(ai_text)
        with open("ai_generated_ads.txt", "w", encoding="utf-8") as f:
            f.write(ai_text)
        print("\n✅ Success! Content saved to 'ai_generated_ads.txt'")        
    except Exception as e:
        print(f"❌ Generation Error: {e}")
if __name__ == "__main__":
    active_model = get_working_model(API_KEY)
    
    if active_model:
        generate_marketing_content(API_KEY, active_model)
    else:
        print("\n[Critical] Could not find any active AI models. Check your API Key and internet connection.")