import json
import os

import ee
import folium
from core.config import MEDIA_DIR, PALETTE

from instruments.folium_instruments import (add_ee_layer, addNdvi,
                                            reverse_coordinates)

folium.Map.add_ee_layer = add_ee_layer


def geojson_to_ndvi_image(geojson, id):
    geometry = geojson['features'][0]['geometry']
    coordinates = geometry['coordinates'][0]
    reversed_coords = reverse_coordinates(coordinates)
    coordinates = json.loads(
        str(coordinates).replace(' ', '').replace('\n', ''))
    if geometry['type'].lower() == 'polygon':
        polygon = ee.Geometry.Polygon(coordinates)
    # Create folium map, and get ee image collection
    Map = folium.Map(zoom_control=False)
    image = (ee.ImageCollection('LANDSAT/LC09/C02/T1_TOA')
             .filterDate('2020-01-01', '2022-12-31')
             .filterBounds(polygon)
             .limit(2, 'CLOUD_COVER')
             )
    # get ndvi for collection
    image = image.map(addNdvi)
    # add layer to Map
    vis_parameters = {'min': -1, 'max': 1, 'palette': PALETTE}
    Map.add_ee_layer(image, vis_parameters, 'ndvi')
    Map.add_child(folium.FitBounds(reversed_coords))
    path = os.path.join(MEDIA_DIR, f'map_{id}.html')
    Map.save(path)
    with open(path) as html:
        map = html.read()
    os.remove(path)
    return map
