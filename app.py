import random
import geopandas as gpd
from shapely.geometry import Point
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class CustomRoot(BoxLayout):
    background_color = ColorProperty() # The ListProperty will also work.

class RandomGPSApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.geojson_file = "vgn.geojson"  # Path to the GeoJSON file
        
        # Load the GeoJSON file and prepare the boundaries
        self.landkreise_gdf = gpd.read_file(self.geojson_file)
        self.bavaria_boundary = self.landkreise_gdf.unary_union
        
        # Latitude and longitude bounds for VGN
        self.min_lat, self.max_lat = 48.8593, 50.5231
        self.min_lon, self.max_lon = 10.0400, 12.5505

    def generate_random_point_in_VGN(self):
        while True:
            # Generate random latitude and longitude
            latitude = random.uniform(self.min_lat, self.max_lat)
            longitude = random.uniform(self.min_lon, self.max_lon)
            
            # Create a Point object
            random_point = Point(longitude, latitude)
            
            # Check if the point is within the VGN boundary
            if random_point.within(self.bavaria_boundary):
                return latitude, longitude

    def build(self):
        # Main layout
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # Label to display coordinates
        self.coord_label = Label(text="Press 'Generate' for GPS Coordinates", font_size='20sp')
        layout.add_widget(self.coord_label)
        
        # Button to generate coordinates
        generate_button = Button(text="Generate Random GPS", font_size='20sp', size_hint=(1, 0.2))
        generate_button.bind(on_press=self.update_coordinates)
        layout.add_widget(generate_button)
        
        return layout

    def update_coordinates(self, instance):
        lat, lon = self.generate_random_point_in_VGN()
        self.coord_label.text = f"Latitude:    {lat:.4f}\nLongitude: {lon:.4f}"

if __name__ == "__main__":
    RandomGPSApp().run()