import random
import geopandas as gpd
from shapely.geometry import Point
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

class region(object):

    def __init__(self, gdf_file):
        self.gdf = gpd.read_file(gdf_file)
        self.boundary = self.gdf.unary_union
        self.lat_range, self.lon_range = self.get_extremes()
        print (f"Lat range: {self.lat_range[0]:.4f} {self.lat_range[1]:.4f}")
        print (f"Lon range: {self.lon_range[0]:.4f} {self.lon_range[1]:.4f}")

    # Extract extreme coordinates
    def get_extremes(self):
        x_coords = []
        y_coords = []
        
        for geom in self.gdf.geometry:
            if geom.geom_type == "Polygon":  # Check if geometry is a Polygon
                x, y = geom.exterior.xy  # Extract exterior coordinates
                x_coords.extend(x)
                y_coords.extend(y)
            elif geom.geom_type == "MultiPolygon":  # Handle MultiPolygon
                for polygon in geom.geoms:
                    x, y = polygon.exterior.xy
                    x_coords.extend(x)
                    y_coords.extend(y)
    
        lat_range = [np.min(y_coords), np.max(y_coords)]
        lon_range = [np.min(x_coords), np.max(x_coords)]
    
        return lat_range, lon_range
    
    # Function to generate a random GPS coordinate within the VGN boundary
    def generate_random_point(self):
        while True:
            # Generate random latitude and longitude
            latitude  = random.uniform(self.lat_range[0], self.lat_range[1])
            longitude = random.uniform(self.lon_range[0], self.lon_range[1])
            
            # Create a Point object
            random_point = Point(longitude, latitude)
            
            # Check if the point is within the boundary
            if random_point.within(self.boundary):
                return latitude, longitude

    # Draw n test points to verify the algorithm
    def test_generation(self, n):
        lats = []; lons = []
        for i in tqdm( range (0,n) ):
            latitude, longitude = self. generate_random_point()
            lats.append(latitude)
            lons.append(longitude)
        plt.plot(lats, lons, "."); plt.show()
    
