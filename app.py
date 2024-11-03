from flask import Flask, render_template, jsonify
import sqlite3

app = Flask(__name__)

# Serve the index.html on the main route
@app.route('/')
def index():
    return render_template('index.html')

# API route to get all housing listings from the database
@app.route('/api/listings', methods=['GET'])
def get_listings():
    conn = sqlite3.connect('OrangeNestListing_test.db')  # Use the correct database path
    conn.row_factory = sqlite3.Row  # This allows us to fetch rows as dictionaries
    cur = conn.cursor()
    
    # Query to get all listings
    cur.execute("SELECT * FROM listinginfo")
    rows = cur.fetchall()
    
    # Convert row objects to dictionaries, extracting latitude, longitude, name, and price
    listings = [{
        "latitude": row["latitude"],
        "longitude": row["longitude"],
        "name": row["listing_name"],
        "price": row["price"]
    } for row in rows]
    
    conn.close()
    
    return jsonify(listings)

if __name__ == '__main__':
    app.run(debug=True)

