import requests
import json

API_KEY = "89823903-7c38-4823-8cea-41d0eb2a1a2a"

BASE_URL = "https://api.balldontlie.io/v1"
BASE_STATS_URL = f"{BASE_URL}/stats?seasons[]=2023&per_page=100"
player_url = f"{BASE_URL}/players?per_page=100"
url = f"{BASE_STATS_URL}&player_ids[]=95"

# Set up the headers for the request
headers = {
    "Authorization": f"{API_KEY}"
}

# Make the GET request

response = requests.get(url, headers=headers)

# # Check the status code of the response
# if response.status_code == 200:
#     # Parse the JSON data
#     data = response.json()
#     with open('file2.json', 'w') as file:
#         json.dump(data, file, indent=4)
#     print(data)
# else:
#     print(f"Request failed with status code {response.status_code}")