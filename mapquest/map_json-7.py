# integrated ETA as new feature into application
import requests
import urllib.parse
from datetime import datetime, timedelta

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "d2OAzEC0bXBe0A6NHl7gBwWqrvTvvjZt"

while True:
    orig = input("Starting Location: ")
    if orig.lower() in ["quit", "q"]:
        break
    
    dest = input("Destination: ")
    if dest.lower() in ["quit", "q"]:
        break

    # URL for API call
    url = main_api + urllib.parse.urlencode({"key": key, "from": orig, "to": dest})
    print("URL: " + url)
    
    # Send request and parse response
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    
    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print("=============================================")
        print("Directions from " + orig + " to " + dest)
        print("ETA: " + json_data["route"]["formattedTime"])
        print("Kilometers: " + "{:.2f}".format(json_data["route"]["distance"] * 1.6))  

        # Extract trip duration in hours, minutes, and seconds
        duration = json_data["route"]["formattedTime"]
        hours, minutes, seconds = map(int, duration.split(":"))
        trip_duration = timedelta(hours=hours, minutes=minutes, seconds=seconds)
        
        # Calculate ETA
        current_time = datetime.now()
        eta = current_time + trip_duration
        print("Current Time: " + current_time.strftime("%Y-%m-%d %H:%M:%S"))
        print("ETA (Estimated Time of Arrival): " + eta.strftime("%Y-%m-%d %H:%M:%S"))
        
        print("=============================================")

        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print(each["narrative"] + " (" + "{:.2f}".format(each["distance"] * 1.61) + " km)")
            print("=============================================\n")
    
    elif json_status == 402:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
        print("**********************************************\n")
    
    elif json_status == 611:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Missing an entry for one or both locations.")
        print("**********************************************\n")
    
    else:
        print("************************************************************************")
        print("For Status Code: " + str(json_status) + "; Refer to:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("************************************************************************\n")