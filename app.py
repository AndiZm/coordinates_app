import streamlit as st
import random
import geopandas as gpd
from shapely.geometry import Point

# Custom CSS to style Streamlit messages
st.markdown("""
    <style>
    div.stAlert {
        background-color: #ffffff; /* Wtihe background */
        color: #000080; /* Navy text color */
        border-radius: 0px; /* Rounded corners */
        padding: 0px; /* Padding inside the message box */
    }
    </style>
    """, unsafe_allow_html=True)

# Function to generate random GPS coordinates
def generate_random_point_in_VGN(bavaria_boundary, min_lat, max_lat, min_lon, max_lon):
    while True:
        # Generate random latitude and longitude
        latitude = random.uniform(min_lat, max_lat)
        longitude = random.uniform(min_lon, max_lon)

        # Create a Point object
        random_point = Point(longitude, latitude)

        # Check if the point is within the VGN boundary
        if random_point.within(bavaria_boundary):
            return latitude, longitude

# Load GeoJSON file
geojson_file = "vgn.geojson"
landkreise_gdf = gpd.read_file(geojson_file)
bavaria_boundary = landkreise_gdf.unary_union

# Latitude and longitude bounds for VGN
min_lat, max_lat = 48.8593, 50.5231
min_lon, max_lon = 10.0400, 12.5505

# Streamlit UI
st.title("Random GPS Coordinate Generator for VGN")
st.write("Click the button to generate a random GPS coordinate within the VGN region.")

if st.button("Generate Random GPS"):
    lat, lon = generate_random_point_in_VGN(bavaria_boundary, min_lat, max_lat, min_lon, max_lon)
    st.success(f"{lat:.4f}, {lon:.4f}")
