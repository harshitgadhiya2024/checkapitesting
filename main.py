import requests
import json
from flask import Flask, render_template

app = Flask(__name__)

def get_news_data(page):
    try:
        url = f"https://www.overnightmountings.com/api/rest/itembom?page_number={page}&number_of_items=30&category_id=134&diamond_quality=B"
        payload = {}
        headers = {'Cookie': 'PHPSESSID=072072e39bd6ad0832c2cf79bd631612'}
        response = requests.request("GET", url, headers=headers, data=payload)
        data_main = json.loads(response.text)
        return data_main
    except Exception as e:
        print(e)
        return {}

@app.route('/<pag_no>')
def get_data(pag_no):
    # Retrieve data from API
    all_main_data = get_news_data(int(pag_no))
    
    # Initialize lists to store image, video, and other data
    items = []

    # Loop through each item in the data and categorize the data
    for item in all_main_data.values():
        if isinstance(item, dict):
            item_data = {
                "images": [],
                "videos": [],
                "other_data": []
            }
            data_keys = list(item.keys())
            for key in data_keys:
                if key.lower() == "images":
                    if isinstance(item[key], list):
                        item_data["images"].extend(item[key])
                elif key.lower() == "default_image_url":
                    item_data["images"].append(item[key])
                elif key.lower() == "videos":
                    if isinstance(item[key], list):
                        item_data["videos"].extend(item[key])
                    else:
                        item_data["videos"].append(item[key])
                else:
                    item_data["other_data"].append((key, item[key]))
            items.append(item_data)

    # Render the template with the categorized data
    return render_template("index.html", items=items, pag_no=pag_no,prev=int(pag_no)-1, next=int(pag_no)+1)

@app.route('/')
def get_datanew():
    # Retrieve data from API
    all_main_data = get_news_data(int(1))
    
    # Initialize lists to store image, video, and other data
    items = []

    # Loop through each item in the data and categorize the data
    for item in all_main_data.values():
        if isinstance(item, dict):
            item_data = {
                "images": [],
                "videos": [],
                "other_data": []
            }
            data_keys = list(item.keys())
            for key in data_keys:
                if key.lower() == "images":
                    if isinstance(item[key], list):
                        item_data["images"].extend(item[key])
                elif key.lower() == "default_image_url":
                    item_data["images"].append(item[key])
                elif key.lower() == "videos":
                    if isinstance(item[key], list):
                        item_data["videos"].extend(item[key])
                    else:
                        item_data["videos"].append(item[key])
                else:
                    item_data["other_data"].append((key, item[key]))
            items.append(item_data)

    # Render the template with the categorized data
    return render_template("index.html", items=items, pag_no=1,prev=int(1)-1, next=int(1)+1)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5454)
