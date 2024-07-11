import requests
import json
from flask import Flask, render_template

app = Flask(__name__)

def get_news_data(page):
    try:
        url = f"https://www.overnightmountings.com/api/rest/itembom?page_number=page&number_of_items=15&category_id=134&diamond_quality=B"
        headers = {'Cookie': 'PHPSESSID=072072e39bd6ad0832c2cf79bd631612'}
        response = requests.get(url, headers=headers)
        data_main = response.json()
        return data_main
    except Exception as e:
        print(e)
        return {}

@app.route('/<int:page>')
def get_data(page=1):
    # Retrieve data from API
    all_main_data = get_news_data(page)
    
    # Initialize a list to store items with names, images, and videos
    items = []

    # Loop through each item in the data and extract names, images, and videos
    for item in all_main_data.values():
        if isinstance(item, dict):
            item_data = {
                "name": item.get("name", "Unknown Name"),
                "id": item.get("entity_id"),
                "images": [],
                "videos": []
            }
            
            # Extract images
            if "images" in item:
                item_data["images"].extend(item["images"].values())
            
            # Extract videos
            if "videos" in item:
                if isinstance(item["videos"], list):
                    item_data["videos"].extend(item["videos"])
                else:
                    item_data["videos"].append(item["videos"])

            items.append(item_data)

    # Render the template with the structured data
    return render_template("demo.html", items=items, page=page)

@app.route('/')
def index():
    return get_data(1)


if __name__ == '__main__':
    app.run(debug=True)
