# @author Filip Durca
# This is the main file that compiles the data

# import
import requests
import json

# Variables
URL = "https://data.ontario.ca/api/3/action/datastore_search?resource_id=455fd63b-603d-4608-8216-7d8647f43350&limit=300000"
request = requests.get(URL)
data = request.json();
d = data.get("result")
records = d.get("records")
groups = {}
groups["Ontario"] = 0;

# Outer loop
while(True):
    # Get the sort parameter
    sort = input("Sort: ")

    if (sort == "exit"):
        exit(0)

    # Loop through each record
    for record in records:
        if record["Outcome1"] == "Not Resolved":
            if record.get(sort) not in groups:
                groups[record.get(sort)] = 1
            else:
                groups[record.get(sort)] = groups[record.get(sort)] + 1
            groups["Ontario"] = groups["Ontario"] + 1

    # Print
    print("Sorted by: ", sort)
    for s in sorted(groups, key = groups.get, reverse = True):
        print('{:40s}{:7d}'.format(s, groups.get(s)))

    print("-------------------------------------------------------------")

    groups.clear()
    groups["Ontario"] = 0