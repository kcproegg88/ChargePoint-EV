import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
API_KEY = os.getenv('API_KEY')
DIRECTIONS_API_URL = "https://maps.googleapis.com/maps/api/directions/json"

params = {
    "origin": "43.2605, -79.8899 ",  # San Francisco coordinates
    "destination": "43.2625, -79.8999 ",  # Example destination
    "departure_time": "now",  # Use live traffic data
    "key": API_KEY,
    "traffic_model": "best_guess",  # Options: best_guess, pessimistic, optimistic
}

# Make the API request
response = requests.get(DIRECTIONS_API_URL, params=params)

if response.status_code == 200:
    data = response.json()

    # Parse relevant information
    if data["status"] == "OK":
        route = data["routes"][0]["legs"][0]
        print("Start Address:", route["start_address"])
        print("End Address:", route["end_address"])
        print("Duration (normal):", route["duration"]["text"])
        print("Duration in traffic:", route["duration_in_traffic"]["text"])
    else:
        print("Error:", data["status"])
else:
    print("Failed to connect to the API:", response.status_code)

print(response)

# next: to use traffic data and extrapolate EV density. Might need to find some datasets to run some models for this. 
# Connect with database to list partnered charging locations. 