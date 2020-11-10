# @author Filip Durca
# This is the main file that compiles the data

# import
import requests
import json

# Variables
URL = "https://data.ontario.ca/api/3/action/datastore_search?resource_id=455fd63b-603d-4608-8216-7d8647f43350&limit=100000"
request = requests.get(URL)
data = request.json();
d = data.get("result")
records = d.get("records")


for record in records:
