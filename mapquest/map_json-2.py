import requests
import urllib.parse 

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Washington, D.C."
dest = "Baltimore, Md"
key = "d2OAzEC0bXBe0A6NHl7gBwWqrvTvvjZt"

url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})

print("URL ", (url))
json_data = requests.get(url).json()
json_status = json_data["info"]["statuscode"]
if json_status == 0:
    print("API Status: " + str(json_status) + " = A successful route call.\n")
