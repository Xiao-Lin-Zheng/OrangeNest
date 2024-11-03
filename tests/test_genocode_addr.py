from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

# Initialize geolocator
geolocator = Nominatim(user_agent="orangenest_locator")
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)

# Define the specific address to test
full_address = "300 E Washington St, Syracuse, 13202"

# Fetch the coordinates for the address
location = geocode(full_address)

# Print the latitude and longitude if location is found
if location:
    print("Address:", full_address)
    print("Latitude:", location.latitude)
    print("Longitude:", location.longitude)
else:
    print("Location not found for the address.")
