#! python3

##############
# Analysing location data
##############
# import googlemaps
# gmaps = googlemaps.Client(key='AIzaSyC0Q1JQJdZeyhg8TDTs2o3YsQty7ZqSHFU')
# address = '1600 Amphitheatre way Parkway, Mountain View, CA'
# geocode_result = gmaps.geocode(address)
# print(geocode_result[0]['geometry']['location'].values())  # Displays Latitude and Longitude

##############
# Spatial Data analysis - finding the closest object
##############
import pandas as pd
from geopy.distance import distance
locations = [
    ('cab_26', 43.602508,39.715685, '14:47:44'),
    ('cab_112', 43.582243,39.752077, '14:47:55'),
    ('cab_26', 43.607480,39.721521, '14:49:11'),
    ('cab_112', 43.579258,39.758944, '14:49:51'),
    ('cab_112', 43.574906,39.766325, '14:51:53'),
    ('cab_26', 43.612203,39.720491, '14:52:48'),
]

df = pd.DataFrame(locations, columns=['cab', 'lat', 'lon', 'tm'])
latest_rows = df.sort_values(['cab', 'tm'], ascending=False).drop_duplicates('cab')  # Finf most recent coords
latest_rows = latest_rows.values.tolist()
# print(latest_rows)
pick_up = 43.578854, 39.754995
for i, row in enumerate(latest_rows):
    dist = distance(pick_up, (row[1], row[2])).m
    print(row[0] + ':', round(dist))
    latest_rows[i].append(round(dist))
closest = min(latest_rows, key=lambda x: x[4])
# print('The closest cab is: ', closest[0], ' - the distance in meters: ', closest[4])

##############
# Finding objects in a certain area
##############

# from shapely.geometry import Point, Polygon
# coords = [
#     (46.082991, 38.987384),
#     (46.075489, 38.987599),
#     (46.079395, 38.997684),
#     (46.073822, 39.007297),
#     (46.081741, 39.008842)
# ]
# poly = Polygon(coords)
# cab_26 = Point(46.073852, 38.991890)
# cab_112 = Point(46.078228, 39.003949)
# pick_up = Point(46.080074, 38.991289)
# print('cab_26 within the polygon: ', cab_26.within(poly))
# print('cab_112 within the polygon: ', cab_112.within(poly))
# print('pickup within the polygon: ', pick_up.within(poly))

##############
# Finding the closest + finding the object in a certain area (combo of the above 2)
##############

# from shapely.geometry import Point, Polygon
# coords = [
#     (46.082991, 38.987384),
#     (46.075489, 38.987599),
#     (46.079395, 38.997684),
#     (46.073822, 39.007297),
#     (46.081741, 39.008842)
# ]
# poly = Polygon(coords)
# cab_26 = Point(46.073852, 38.991890)
# pick_up = Point(46.080074, 38.991289)
# entry_point = Point(46.075357, 39.000298)
#
# if cab_26.within(poly):
#     dist = distance((pick_up.x, pick_up.y), (cab_26.x, cab_26.y)).m
# else:
#     dist = distance((cab_26.x, cab_26.y), (entry_point.x, entry_point.y)).m + \
#            distance((entry_point.x, entry_point.y), (pick_up.x, pick_up.y)).m
# print(round(dist))

##############
# Combining spatial and non-spatial data
##############

# import pandas as pd
# orders = [
#     ('order_039', 'open', 'cab_14'),
#     ('order_034', 'open', 'cab_79'),
#     ('order_033', 'open', 'cab_104'),
#     ('order_026', 'closed', 'cab_79'),
#     ('order_021', 'open', 'cab_45'),
#     ('order_018', 'closed', 'cab_26'),
#     ('order_008', 'closed', 'cab_112'),
# ]
# df_orders = pd.DataFrame(orders, columns=['order', 'status', 'cab'])
# df_orders_open = df_orders[df_orders['status'] == 'open']
# unavailable_list = df_orders_open['cab'].values.tolist()
# print(unavailable_list)

# from geopy.distance import distance
# pick_up = 46.083822, 38.967845
# cab_26 = 46.073852, 38.991890
# cab_112 = 46.078228, 39.003949
# cab_104 = 46.071226, 39.004947
# cab_14 = 46.004859, 38.095825
# cab_79 = 46.088621, 39.033929
# cab_45 = 46.141225, 39.124934
# cabs = {'cab_26': cab_26, 'cab_112': cab_112, 'cab_14': cab_14, 'cab_104': cab_104, 'cab_79': cab_79, 'cab_45': cab_45}
# dist_list = []
# for cab_name, cab_loc in cabs.items():
#     if cab_name not in unavailable_list:
#         dist = distance(pick_up, cab_loc).m
#         dist_list.append((cab_name, round(dist)))
# print(dist_list)
# print(min(dist_list, key=lambda x :x[1]))

##############
# Joining spatial and non-spatial datasets
##############
# Now cabs have an option to whether they carry a babyseat

cabs_list = [ # cabs with 1 in second column contain a baby-seat
    ('cab_14', 1),
    ('cab_79', 0),
    ('cab_104', 0),
    ('cab_45', 1),
    ('cab_26', 0),
    ('cab_112', 1)
]
df_cabs = pd.DataFrame(cabs_list, columns=['cab', 'seat'])
df_dist = pd.DataFrame(dist_list, columns=['cab', 'dist'])
df = pd.merge(df_cabs, df_dist, on='cab', how='inner')
result_list = list(df.itertuples(index=False, name=None))  # convert DF to tuples, filter to show only cabs with 1 seat
result_list = [x for x in result_list if x[1] == 1]
# print(min(result_list, key=lambda x: x[2]))  # determine the row with the lowest value in 'dist' field
