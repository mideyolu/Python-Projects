

```markdown
# Phone Number Location Tracker

This is a simple Flask web application that allows users to track the location and service provider of a phone number. The application utilizes the `phonenumbers` library for parsing phone numbers, `geocoder` for obtaining location information, and `OpenCageGeocode` for geocoding. The results are displayed on an interactive map created with `folium`.

## Setup

### Prerequisites

- Python 3.x
- Flask
- phonenumbers
- opencage
- folium
- dotenv

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/mideyolu/Python-Projects/blob/main/Location-Tracker.gi
   cd Location-Tracker
   ```

2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root and add your OpenCage API key:

   ```
   You can get your api key from here
   https://opencagedata.com/
   ```
   ```
   OPEN_CAGE_API=your_opencage_api_key_here
   ```

### Running the Application

Run the Flask application:

```bash
python location.py
```

The application will be accessible at [http://localhost:5000/](http://localhost:5000/).

## Usage

1. Access the home page at [http://localhost:5000/](http://localhost:5000/).
2. Enter a phone number with the country code in the provided form (i.e +1184746352877).
3. Click on the "Track Location" button.
4. The result page will display the location, service provider, and an interactive map showing the exact location.

## Files

- **location.py**: The main Flask application file.
- **index.html**: HTML template for the home page.
- **result.html**: HTML template for displaying the results.
- **static/styles.css**: CSS file for styling the HTML templates.

## Dependencies

- Flask
- phonenumbers
- opencage
- folium
- dotenv


