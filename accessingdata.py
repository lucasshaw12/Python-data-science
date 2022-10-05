#! python3
# Accessing data files (txt, API, JSON, CSV, HTML)

##############
# Text Files .txt
##############

# path = 'excerpt.txt'
# with open(path, 'r') as f:
#     content = f.read()
#     print(content)

# with open(path, 'r') as f:
#     for i, line in enumerate(f):
#         if line.strip():
#             print(f'line {i}: ', line.strip())

# Using list comprehension to add each line to a list
# with open(path, 'r') as f:
#     lst = [line.strip() for line in f if line.strip()]
# print(lst)

##############
# Tabular Data Files
##############

import csv

# path = 'cars.csv'

# Using DictReader()
# with open(path, 'r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     cars = []
#     for row in csv_reader:
#         cars.append(dict(row))
# print(cars)

# using reader()
# with open(path, 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)
#     cars = []
#     for row in csv_reader:
#         cars.append(row)
# print(cars)

##############
# Binary Files
##############

# image = 'uk_average_house_price.png'
# with open(image, 'rb') as binary_file:
#     content = binary_file.read()
# print(len(content))

##############
# Exporting Data to Files
##############

# path = 'cars.csv'
# for row in cars:
#     print(list(row.values()))

# to_update = ['1999', 'Chevy', 'Venture']
# new_price = '4500.00'
# with open(path, 'w') as csv_file:
#     fieldnames = cars[0].keys()
#     writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
#     writer.writeheader()
#     for row in cars:
#         if set(to_update).issubset(set(row.values())):
#             row['Price'] = new_price
#         writer.writerow(row)


##############
# HTTP Requests urllib3
##############

# import urllib3
# http = urllib3.PoolManager()
# r = http.request('GET', 'https://github.com/pythondatabook/sources/blob/main/ch4/excerpt.txt')
# for i, line in enumerate(r.data.decode('utf-8').split('\n')):
#     if line.strip():
#         print(f'Line {i}', line.strip())


##############
# HTTP Requests using Requests
##############

# import requests
# r = requests.get('https://github.com/pythondatabook/sources/blob/main/ch4/excerpt.txt')
# r.raise_for_status()
# for i, line in enumerate(r.text.split('\n')):
#     if line.strip():
#         print(f'Line {i}:', line.strip())


##############
# Importing nested JSON Structures
##############

# data = [{'Emp': 'Jeff',
#          'POs': [{'Pono': 2608, 'Total': 35},
#                  {'Pono': 2617, 'Total': 35},
#                  {'Pono': 2620, 'Total': 139}
#                  ]},
#         {'Emp': 'Jane',
#          'POs': [{'Pono': 2621, 'Total': 95},
#                  {'Pono': 2626, 'Total': 218}
#                  ]
#          }]
#
# import json
# import pandas as pd
#
# df = pd.json_normalize(data, 'POs', 'Emp').set_index('Emp', 'Pono')
# print(df)
#
# ##############
# # Converting dataframe to JSON
# ##############
#
# df = df.reset_index()
# json_doc = (df.groupby(['Emp'], as_index=True)
#             .apply(lambda x: x[['Pono', 'Total']]
#             .to_dict('records'))
#             .reset_index()
#             .rename(columns={0: 'PO'})
#             .to_json(orient='records'))
# print(json.dumps(json.loads(json_doc), indent=2))

##############
# Obtaining Data from Stoq using Pandas data_reader
##############

# import pandas_datareader.data as pdr
# # print(dir(pdr))
# spx_index = pdr.get_data_stooq('^SPX', '2022-01-03', '2022-01-10')
# print(spx_index)