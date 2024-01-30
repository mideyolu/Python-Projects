# from flask import Flask, render_template, request
# import phonenumbers
# from phonenumbers import geocoder, carrier
# from opencage.geocoder import OpenCageGeocode
# import folium
# from dotenv import load_dotenv
# import os

# # Loading the environment variable
# load_dotenv()

# #setting up the Flask app
# app = Flask(__name__)

# #loading the api key
# Key = os.getenv("OPEN_CAGE_API")

# #defining routes

# #index (Home page)
# @app.route('/')
# def index():
#     return render_template('index.html')

# #result page
# @app.route('/result', methods=['POST'])
# def result():
#     if request.method == 'POST':
#         #getting Location Information:
#         number = request.form['phone_number']
#         phoneNumber = phonenumbers.parse(number, None)

#         yourLocation = geocoder.description_for_number(phoneNumber, "en")
#         yourServiceProvider = carrier.name_for_number(phoneNumber, "en")

#         #geocoding with OpenCage:
#         geocoder_opencage = OpenCageGeocode(Key)
#         query = str(yourLocation)
#         results = geocoder_opencage.geocode(query)

#         lat = results[0]['geometry']['lat']
#         lng = results[0]['geometry']['lng']

#         #map creataion with folium
#         myMap = folium.Map(location=[lat, lng], zoom_start=9)

#         #adding Marker to the Map:
#         folium.Marker([lat, lng], popup=yourLocation).add_to(myMap)
#         folium.TileLayer("OpenStreetMap").add_to(myMap)
#         folium.LayerControl().add_to(myMap)
        
#         #rendering Map HTML:
#         map_html = myMap.get_root().render()


#         return render_template('result.html', 
#                                location=yourLocation, 
#                                service_provider=yourServiceProvider, 
#                                map_html=map_html)

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, render_template, request
import phonenumbers
from phonenumbers import geocoder, carrier
from opencage.geocoder import OpenCageGeocode
import folium
from dotenv import load_dotenv
import os

# Loading the environment variable
load_dotenv()

# Setting up the Flask app
app = Flask(__name__)

# Loading the API key
Key = os.getenv("OPEN_CAGE_API")

# Defining routes

# Index (Home page)
@app.route('/')
def index():
    return render_template('index.html')

# Result page
@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        # Getting Location Information
        number = request.form['phone_number']
        phoneNumber = phonenumbers.parse(number, None)

        yourLocation = geocoder.description_for_number(phoneNumber, "en")
        yourServiceProvider = carrier.name_for_number(phoneNumber, "en")

        # Geocoding with OpenCage
        geocoder_opencage = OpenCageGeocode(Key)
        query = str(yourLocation)
        results = geocoder_opencage.geocode(query)

        lat = results[0]['geometry']['lat']
        lng = results[0]['geometry']['lng']

        # Map creation with Folium
        myMap = folium.Map(location=[lat, lng], zoom_start=9)

        # Adding Marker to the Map with Popup displaying both location and service provider
        popup_content = f"{yourLocation}, {yourServiceProvider}"
        folium.Marker([lat, lng], popup=popup_content).add_to(myMap)

        folium.TileLayer("OpenStreetMap").add_to(myMap)
        folium.LayerControl().add_to(myMap)

        # Rendering Map HTML
        map_html = myMap.get_root().render()

        return render_template('result.html',
                               location=yourLocation,
                               service_provider=yourServiceProvider,
                               map_html=map_html)

if __name__ == '__main__':
    app.run(debug=True)
