from shapely.geometry import Polygon, Point
import numpy as np
import random 

# Network Polygon
netPoly = Polygon([
    (39.267732266577795, -76.79912666240163),
    (39.202143545427270, -76.85878560274975),
    (39.209267634946656, -76.88718021114587),
    (39.250097318923764, -76.85233935397152)
])

def polygon_random_points(poly, num_points):
    """
    Credits:
    - https://medium.com/the-data-journal/a-quick-trick-to-create-random-lat-long-coordinates-in-python-within-a-defined-polygon-e8997f05123a
    """
    min_x, min_y, max_x, max_y = poly.bounds

    points = []
    while len(points) < num_points:
        random_point = Point([random.uniform(min_x, max_x),
                            random.uniform(min_y, max_y)])
        if (random_point.within(poly)):
            points.append(random_point)
    return points

# Choose the number of points desired. This example uses 20 points. 
points = polygon_random_points(netPoly,20)
# Printing the results.
for p in points:
    print(f"{p.x},{p.y}")