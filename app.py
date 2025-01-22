import streamlit as st
import random
import geopandas as gpd
from shapely.geometry import Point
from src import *

vgn = region("vgn.geojson")
#bayern = region("bayern.geojson")

# Streamlit UI
st.title("Random GPS Coordinate Generator")
st.write("Click the button to generate a random GPS coordinate within the region you prefer.")

if st.button("VGN"):
    lat, lon = vgn.generate_random_point()
    st.success(f"{lat:.4f}, {lon:.4f}")

#if st.button("Bavaria"):
#    lat, lon = bayern.generate_random_point()
#    st.success(f"{lat:.4f}, {lon:.4f}")
