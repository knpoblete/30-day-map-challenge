import geopandas as gpd
import folium

# https://data.humdata.org/dataset/philippines-healthsites

def set_font():
    return """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@100;300;400;500;700&display=swap');
        html, body, [class*="css"]  {
        font-family: "Roboto", sans-serif !important;
        font-weight: 300;
        };
        .st-ae {
            font-family: "Roboto", sans-serif !important;
        }
    </style>

    """

def set_font(text, size="h3"):
    outstring = f"""<{size} style="color:#151E3F;">{text}</{size}>"""
    return outstring

def read_data(filepath):
    data = gpd.read_file(filepath)
    data['lon'] = data['geometry'].get_coordinates(ignore_index=True).x
    data['lat'] = data['geometry'].get_coordinates(ignore_index=True).y
    data['location'] = list(zip(data['lat'],data['lon']))
    hospitals = data[data['amenity']=='hospital']
    return hospitals

def show_map(df):
    map = folium.Map(location=[13, 122], 
                 zoom_start=5,
                 tiles='https://api.mapbox.com/styles/v1/knpoblete/clgi3uciu001801ln65r8ors6/tiles/256/{z}/{x}/{y}@2x?access_token=pk.eyJ1Ijoia25wb2JsZXRlIiwiYSI6ImNsZ2k5NGE4ZTBpc2IzY2xmemgwdWl5NXkifQ.UQ55c1MEZb-mQV-x66gKIQ',
                 attr='Mapbox Light')

    feature_group = folium.FeatureGroup("Locations")

    for lat, lon, name in zip(list(df['lat']), list(df['lon']), list(df['location'])):
        feature_group.add_child(folium.Marker(location=[lat,lon],
                                            popup=name,
                                            icon=folium.Icon(color="red", icon="glyphicon glyphicon-plus", size=0.5)))

    map.add_child(feature_group)

    return map
