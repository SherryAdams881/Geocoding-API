# Geocoding-API
# Geolocation Utility

This is a command-line utility that fetches latitude, longitude, and location details using the OpenWeather Geocoding API.

## Prerequisites

- Python 3.x
- `requests` and `pytest` libraries

## Installation

1. Clone the repository:
   ```sh
   git clone <repository_url>
   cd <repository_name>
   ```
2. Install dependencies:
   ```sh
   pip install requests pytest
   ```

## Usage

Run the utility with city/state or zip codes as arguments:

```sh
python geoloc_util.py "Madison, WI" "10001"
```

Example Output:

```
Madison, WI, US: Latitude 43.0731, Longitude -89.4012
10001, US: Latitude 40.7128, Longitude -74.0060
```

## Running Tests

To run integration tests, execute:

```sh
pytest geoloc_util.py
```

This will verify that the utility correctly retrieves geolocation data for valid locations and handles invalid inputs appropriately.

## API Key

The utility uses the OpenWeather API key (`f897a99d971b5eef57be6fafa0d83239`). If needed, you can replace it with your own key in the script.

## Notes

- The utility supports only U.S. locations.
- If multiple results are returned by the API, the first result is used.
- If an invalid location is provided, the utility will indicate that no data was found.

## License

This project is for demonstration purposes only.

