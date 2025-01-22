import streamlit as st
import random
import geopandas as gpd
from shapely.geometry import Point
from src import *

vgn = region("vgn.geojson")

# Streamlit UI
st.title("Random GPS Coordinate Generator for VGN")
st.write("Click the button to generate a random GPS coordinate within the VGN region.")

if st.button("Generate Random GPS"):
    lat, lon = vgn.generate_random_point()
    st.success(f"Hurra: {lat:.4f}, {lon:.4f}")
