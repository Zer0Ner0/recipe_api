import json
import requests

API_URL = "http://halnova.synology.me:8001/api/v1/add/"
JSON_FILE = "recipes_sample.json"  # Path to your generated JSON file

def upload_recipes():
    with open(JSON_FILE, "r") as f:
        recipes = json.load(f)

    for idx, recipe in enumerate(recipes, start=1):
        try:
            response = requests.post(API_URL, json=recipe)
            if response.status_code in (200, 201):
                print(f"[{idx}] ✅ Uploaded: {recipe['title']}")
            else:
                print(f"[{idx}] ❌ Failed: {recipe['title']} | Status: {response.status_code} | {response.text}")
        except Exception as e:
            print(f"[{idx}] ⚠️ Error uploading {recipe['title']}: {e}")

if __name__ == "__main__":
    upload_recipes()
