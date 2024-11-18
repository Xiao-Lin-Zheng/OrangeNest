import sqlite3
import pandas as pd
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
from geopy import distance
from datetime import datetime
import calendar

def main():
    # Path to the downloaded CSV file from Google Sheets
    # Note: this is specific to a local directory for loading data
    # You do NOT need to run thus script because the database (OrangeNestListings_test.db) is already included in the 'data' folder.
    csv_path = '/Users/xiaolinzheng/Downloads/orangenest_data.csv'
    
    # Connect to the SQLite database
    conn = sqlite3.connect('OrangeNestListings_test.db')
    
    # Read and clean CSV data
    df = pd.read_csv(csv_path)

    # Perform necessary cleaning or transformation
    df = clean_data(df)

    # Insert data into SQLite table
    df.to_sql('listinginfo', conn, if_exists='replace', index=False)

    # Commit and close connection
    conn.commit()
    conn.close()

def clean_data(df):
    # Convert facilities columns to Yes/No or boolean equivalents
    df['air_conditioning'] = df['air_conditioning'].apply(lambda x: 'Yes' if x.lower() in ['yes', 'y'] else 'No')
    df['furnished'] = df['furnished'].apply(lambda x: 'Yes' if x.lower() in ['yes', 'y'] else 'No')
    df['laundry'] = df['laundry'].apply(lambda x: 'Yes' if x.lower() in ['yes', 'y'] else 'No')
    df['parking'] = df['parking'].apply(lambda x: 'Yes' if x.lower() in ['yes', 'y'] else 'No')
    # Generate latitude and longitude based on address information
    df['latitude'], df['longitude'] = zip(*df.apply(geocode_address, axis=1))

    # Calculate distance to Syracuse University
    df['distance_from_su'] = df.apply(calculate_distance_from_school, axis=1)
    df['latitude'] = df['latitude'].astype(float)
    df['longitude'] = df['longitude'].astype(float)
    df['distance_from_su'] = df['distance_from_su'].astype(float)

    # Convert date columns to standard datetime format if necessary
    df['availability'] = df['availability'].apply(convert_to_datetime)

    # Clean column names to match the SQLite table structure
    df = df.rename(columns={
        'listing_name': 'listing_name',
        'street_address': 'street_address',
        'city': 'city',
        'postal_code': 'postal_code',
        'contact': 'contact',
        'bedrooms': 'bedrooms',
        'type_of_accommodation': 'type_of_accommodation',
        'price': 'price',
        'availability': 'availability',
        'air_conditioning': 'air_conditioning',
        'furnished': 'furnished',
        'laundry': 'laundry',
        'parking': 'parking',
        'latitude': 'latitude',
        'longitude': 'longitude',
        'distance_from_su': 'distance_from_su',
        'listing_photo': 'listing_photo'
    })

    return df

def geocode_address(row):
    """
    Generate latitude and longitude based on street address, city, and postal code.
    Uses Geopy's Nominatim geolocator.
    """
    geolocator = Nominatim(user_agent="orangenest_geocoder")
    geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1) 

    # Construct full address from the row data
    full_address = f"{row['street_address']}, {row['city']}, {row['postal_code']}"
    location = geocode(full_address)

    if location:
        return location.latitude, location.longitude
    else:
        return None, None

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

def convert_to_datetime(date_str):
    """
    Convert a given date string to a standard datetime object.
    Supports various formats, modify as needed.
    """
    try:
        if pd.isnull(date_str) or date_str == '':
            return None  # Handle missing or empty dates as None
        return datetime.strptime(str(date_str), "%m/%d/%Y")
    except ValueError:
        return None

if __name__ == "__main__":
    main()
