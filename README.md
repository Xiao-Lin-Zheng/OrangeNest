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

## Pictures  
![Screenshot 2024-11-17 at 7 53 59 PM](https://github.com/user-attachments/assets/0ad0321a-364d-4984-bcda-fde53b337813)  
![Screenshot 2024-11-17 at 7 54 38 PM](https://github.com/user-attachments/assets/5a922c58-e3ce-422a-9012-eb81defbe75f)  
![Screenshot 2024-11-17 at 7 55 12 PM](https://github.com/user-attachments/assets/9fa31da4-0fcc-4068-ba1d-d45312bd3985)  
![Screenshot 2024-11-17 at 7 56 07 PM](https://github.com/user-attachments/assets/41f20567-7d93-4c65-8a1c-b06ab0547c2a)  
![Screenshot 2024-11-17 at 7 56 44 PM](https://github.com/user-attachments/assets/d01deab5-9174-4a6e-bed9-d2066b775400)





