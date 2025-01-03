import requests
import urllib.parse 

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "d2OAzEC0bXBe0A6NHl7gBwWqrvTvvjZt"

while True:
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        break 

    dest = input("Destination: ")
    if dest == "quit" or dest == "q":
        break


    avg_mpg = float(input("Enter your vehicle's average miles per gallon (MPG): "))


    url = main_api + urllib.parse.urlencode({"key": key, "from": orig, "to": dest})
    print("URL: " + url)


    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    
    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print("=============================================")
        print("Directions from " + orig + " to " + dest)
        print("Trip Duration: " + json_data["route"]["formattedTime"])
        print("Kilometers: " + "{:.2f}".format(json_data["route"]["distance"] * 1.6))  
        print("=============================================")


        distance = json_data["route"]["distance"]  
        fuel_used = distance / avg_mpg  

 
        print("Estimated Fuel Used (Gal): " + str(round(fuel_used, 2)))
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

