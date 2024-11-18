from geopy import distance

def calculate_distance_from_school(row):
    """
    Calculate the distance from the apartment to Syracuse University based on latitude and longitude.
    Syracuse University Coordinates: Latitude = 43.0392, Longitude = -76.1351
    """
    SU_COORDINATES = (43.0392, -76.1351)  # Syracuse University coordinates
    try:
        apartment_coordinates = (row['latitude'], row['longitude'])
        if None not in apartment_coordinates:  # Check if coordinates are valid
            return round(distance.distance(SU_COORDINATES, apartment_coordinates).km, 2)
        else:
            return None
    except:
        return None

# Define the test function
def test_calculate_distance_from_school():
    # Sample coordinate near Syracuse University
    test_row = {'latitude': 43.0492, 'longitude': -76.1401}
    expected_distance = 1.13  # Expected distance in km, rounded to two decimal places
    
    result = calculate_distance_from_school(test_row)
    
    tolerance = 0.1  # Allowable difference of 0.1 km
    assert abs(result - expected_distance) <= tolerance, f"Test failed: Expected {expected_distance}, got {result}"
    print(f"Test passed: Distance is {result} km")

# Run the test function
test_calculate_distance_from_school()