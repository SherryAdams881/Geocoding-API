import argparse
import requests
import pytest

API_KEY = "f897a99d971b5eef57be6fafa0d83239"
BASE_URL = "http://api.openweathermap.org/geo/1.0/"

def get_location_info(location):
    if location.isdigit():  # If the input is a zip code
        url = f"{BASE_URL}zip?zip={location},US&appid={API_KEY}"
    else:  # If the input is a city, state
        url = f"{BASE_URL}direct?q={location}&limit=1&appid={API_KEY}"
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if isinstance(data, list) and data:
            data = data[0]
        if data:
            return {
                "name": data.get("name", "Unknown"),
                "state": data.get("state", ""),
                "country": data.get("country", "Unknown"),
                "lat": data.get("lat"),
                "lon": data.get("lon")
            }
    return None

def main():
    parser = argparse.ArgumentParser(description="Get geolocation data using OpenWeather API")
    parser.add_argument("locations", nargs='+', help="Enter city,state or zip code")
    args = parser.parse_args()
    
    for location in args.locations:
        info = get_location_info(location)
        if info:
            print(f"{info['name']}, {info['state']} {info['country']}: Latitude {info['lat']}, Longitude {info['lon']}")
        else:
            print(f"No data found for {location}")

if __name__ == "__main__":
    main()

# Integration Test Cases
def test_get_location_info():
    # Test with a known city
    result = get_location_info("New York, NY")
    assert result is not None
    assert "lat" in result and "lon" in result
    
    # Test with a known zip code
    result = get_location_info("10001")
    assert result is not None
    assert "lat" in result and "lon" in result
    
    # Test with an invalid location
    result = get_location_info("InvalidCity123")
    assert result is None

def test_invalid_zip_code():
    result = get_location_info("99999")  # Assuming this zip code does not exist
    assert result is None

if __name__ == "__main__":
    pytest.main()
