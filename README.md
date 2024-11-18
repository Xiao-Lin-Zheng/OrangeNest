# OrangeNest

**OrangeNest** is course project designed to help students at Syracuse University find housing near campus!  
**Contributers** Xiao Lin Zheng, Menglu Liu, Guozheng Wang, Qiyu Liu

---

## Structure
- `app.py`: run this and get http://127.0.0.1:5000, which you put this in browser to access the web application
- `index.html`: frontend of the application
- `style.css`: custom styling
- `import_data.py`: script to load and process CSV data into the SQLite database. *(Not required for general use as the database is preloaded.)*
- `data/OrangeNestListings_test.db`: SQLite database containing listing data.
- `static/`: css and image files

### Prerequisites
- Python 3.x
- Flask
- SQLite
- Required Python libraries: `pandas`, `geopy`, `datetime`

### Install
- git clone
- cd orangenest
- pip install flask pandas geopy

In the index.html file, replace the following code with your own Google Maps API key:
<!-- Custom JavaScript for Map and Filtering -->
<script src="https://maps.googleapis.com/maps/api/js?key=YOUR_GOOGLE_MAPS_API_KEY&callback=initMap" async defer></script>

## Run the app
python app.py
