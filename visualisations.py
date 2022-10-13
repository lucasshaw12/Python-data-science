#! python3
# Creating visuals using data

##############
# Plotting with Matplotlib
##############

from matplotlib import pyplot as plt

# Line Graph
# days = ['2021-01-04', '2021-01-05', '2021-01-06', '2021-01-07', '2021-01-08']
# prices = [729.77, 735.11, 755.98, 916.04, 880.02]
# plt.plot(days, prices)
# plt.title('NASDAQ: TSLA')
# plt.xlabel('Date')
# plt.ylabel('USD')
# plt.show()
#
# # Pie Chart
# regions = ['New England', 'Mid-Atalntic', 'Midwest']
# sales = [882703, 532648, 714406]
# plt.pie(sales, labels=regions, autopct='%1.1f%%')
# plt.show()
#
# # Bar chart
# plt.bar(regions, sales)
# plt.xlabel('Regions')
# plt.ylabel('Sales')
# plt.title('Annual sales aggregated on a regional basis')
# plt.show()

##############
# Creating a histogram with subplots
##############
import numpy as np
import matplotlib.ticker as ticker

# salaries = [1215, 1221, 1262, 1267, 1271, 1274, 1275, 1318, 1320, 1324, 1324, 1326, 1337, 1346, 1354, 1355, 1364, 1367, 1372, 1375, 1376, 1378,
#             1378, 1410, 1415, 1415, 1417, 1420, 1422, 1426, 1430, 1434, 1437, 1451, 1454, 1467, 1470, 1473, 1477, 1479, 1480, 1514, 1516, 1522,
#             1529, 1544, 1547, 1554, 1562, 1584, 1595, 1616, 1626, 1717
#             ]
#
# fig, ax = plt.subplots()
# fig.set_size_inches(5.6, 4.2)
# ax.hist(salaries, bins=np.arange(1100, 1900, 50), edgecolor='black', linewidth=1.2)
# formatter = ticker.FormatStrFormatter('$%1.0f')
# ax.xaxis.set_major_formatter(formatter)
# plt.title('Monthly salaries in the sales department')
# plt.xlabel('Salary (bin size = 50')
# plt.ylabel('Frequency')
# plt.show()

##############
# Frequency distributions with Pie Charts
##############
# count, labels = np.histogram(salaries, bins=np.arange(1100, 1900, 50))
# labels = ['$'+str(labels[i])+'-'+str(labels[i+1]) for i, _ in enumerate(labels[1:])]
# non_zero_pos = [i for i, x in enumerate(count) if x !=0]  # Include only nonempty values
# labels = [e for i, e in enumerate(labels) if i in non_zero_pos]
# count = [e for i, e in enumerate(count) if i in non_zero_pos]
# plt.pie(count, labels=labels, autopct='%1.1f%%')
# plt.title('Monthly salaries in the Sales Department')
# plt.show()

##############
# Plotting Pandas data
##############
import pandas as pd
# us_cities = pd.read_csv('src/top-us-cities.csv')
# top_us_cities = us_cities[us_cities.Population.ge(1000000)]  # Rows with population field over 1000000
# top_cities_count = top_us_cities.groupby(['State'], as_index=False).count().rename(columns={'City': 'cities_count'})[['State', 'cities_count']]
# top_cities_count.plot.bar('State', 'cities_count', rot=0)
# plt.xlabel('States')
# plt.ylabel('Top cities count')
# plt.title('Number of Megacities per US state')
# plt.yticks(range(min(top_cities_count['cities_count']),
#                  max(top_cities_count['cities_count'])+1))
# plt.show()
