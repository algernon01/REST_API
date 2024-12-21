import requests
import urllib.parse

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "d2OAzEC0bXBe0A6NHl7gBwWqrvTvvjZt"


avg_mpg = 25  

while True:
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        break
    
    dest = input("Destination: ")
    if dest == "quit" or dest == "q":
        break

    url = main_api + urllib.parse.urlencode({"key": key, "from": orig, "to": dest})
    print("URL: " + url)
    
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    
    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print("=============================================")
        print("Directions from " + orig + " to " + dest)
        print("Trip Duration: " + json_data["route"]["formattedTime"])
        
      
        distance_km = json_data["route"]["distance"]
        distance_miles = distance_km * 0.621371
        print(f"Distance: {distance_miles:.2f} miles")
        
        
        if "fuelUsed" in json_data["route"]:
            fuel_used = json_data["route"]["fuelUsed"]
            print("Fuel Used (Gal): " + str(fuel_used))
        else:
            fuel_used = distance_miles / avg_mpg 
            print(f"Estimated Fuel Used (Gal): {round(fuel_used, 2)}")
        
        print("=============================================")


        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print(each["narrative"] + " (" + "{:.2f}".format(each["distance"] * 0.621371) + " miles)")
        print("=============================================\n")
