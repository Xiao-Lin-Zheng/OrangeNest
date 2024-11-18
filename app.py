from flask import Flask, render_template, jsonify, request
import sqlite3

app = Flask(__name__)

# Route for the index page
@app.route('/')
def index():
    return render_template('index.html')

# Route to get filtered listings
@app.route('/api/filter_listings', methods=['POST'])
def filter_listings():
    # Extract filters from form data
    price_min = request.form.get("lp", 0, type=int)
    price_max = request.form.get("mp", 5000, type=int)
    ac = request.form.get("AC") == '1'
    furnished = request.form.get("Furnished") == '1'
    laundry = request.form.get("LF") == '1'
    parking = request.form.get("Parking") == '1'
    types = [t for t in ["Apartment", "House", "Other"] if request.form.get(t) == t]
    daterange = request.form.get("daterange", "").split(" - ")

    print("Parsed filters:")
    print(f"Price range: {price_min} - {price_max}")
    print(f"Facilities: AC={ac}, Furnished={furnished}, Laundry={laundry}, Parking={parking}")
    print(f"Types: {types}")
    print(f"Date range: {daterange}")

    # Build query dynamically
    conditions = ["price BETWEEN ? AND ?"]
    params = [price_min, price_max]

    if ac:
        conditions.append("air_conditioning = 'Yes'")
    if furnished:
        conditions.append("furnished = 'Yes'")
    if laundry:
        conditions.append("laundry = 'Yes'")
    if parking:
        conditions.append("parking = 'Yes'")

    # Handle accommodation types
    if types:
        type_conditions = " OR ".join([f"type_of_accommodation = ?" for _ in types])
        conditions.append(f"({type_conditions})")
        params.extend(types)

    # Handle availability dates
    if len(daterange) == 2:
        conditions.append("availability BETWEEN ? AND ?")
        params.extend(daterange)

    # Final SQL query
    query = f"SELECT * FROM listinginfo WHERE {' AND '.join(conditions)}"


    # Execute query
    conn = sqlite3.connect('data/OrangeNestListings_test.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(query, params)
    rows = cur.fetchall()
    conn.close()

    # Format rows into JSON
    listings = [dict(row) for row in rows]
    return jsonify(listings)


if __name__ == '__main__':
    app.run(debug=True)
