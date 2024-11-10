import requests
import json

keyword = input("Enter keyword: ")
request = "https://api.tvmaze.com/search/shows?q=" + keyword
response = requests.get(request).json()
#print(json.dumps(response, indent=2))

for a in response:
    show = a['show']
    schedule = show["schedule"]
    country_name = show["network"]["country"]["name"] if show["network"] is not None else "No country"

    print(f"{show["name"]}: {country_name}: {schedule["days"]}: {schedule["time"]}")
