import streamlit as st
import random
import geopandas as gpd
from shapely.geometry import Point
from src import *

if "vgn" not in st.session_state:
    st.session_state.vgn = region("vgn")
if "bavaria" not in st.session_state:
    st.session_state.bavaria = region("bavaria")
if "bavaria_north" not in st.session_state:
    st.session_state.bavaria_north = region("bavaria_north")
if "germany" not in st.session_state:
    st.session_state.germany = region("germany")

vgn = st.session_state.vgn
bavaria = st.session_state.bavaria
bavaria_north = st.session_state.bavaria_north
germany = st.session_state.germany

# Streamlit UI
st.title("Random GPS Coordinate Generator")
st.write("Click the button to generate a random GPS coordinate within the region you prefer.")

if st.button("VGN"):
    lat, lon = vgn.generate_random_point()
    st.success(f"{lat:.4f}, {lon:.4f}")

if st.button("Bavaria"):
    lat, lon = bavaria.generate_random_point()
    st.success(f"{lat:.4f}, {lon:.4f}")
    
if st.button("Bavaria North"):
    lat, lon = bavaria_north.generate_random_point()
    st.success(f"{lat:.4f}, {lon:.4f}")

if st.button("Germany"):
    lat, lon = germany.generate_random_point()
    st.success(f"{lat:.4f}, {lon:.4f}")
