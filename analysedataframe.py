#! python3
# Aggregating and analysing data
import pandas as pd

orders = [
    (9423517, '2022-02-04', 9001),
    (4626232, '2022-02-04', 9003),
    (9423534, '2022-02-04', 9001),
    (9423679, '2022-02-05', 9002),
    (4626377, '2022-02-05', 9003),
    (4626412, '2022-02-05', 9004),
    (9423783, '2022-02-06', 9002),
    (4626490, '2022-02-06', 9004)
]
df_orders = pd.DataFrame(orders, columns=['OrderNo', 'Date', 'Empno'])

details = [
    (9423517, 'Jeans', 'Rip curl', 87.0, 1),
    (9423517, 'Jacket', 'THe North Face', 112.0, 1),
    (4626232, 'Socks', 'Vans', 15.0, 1),
    (4626232, 'Jeans', 'Quiksilver', 82.0, 1),
    (9423534, 'Socks', 'DC', 10.0, 2),
    (9423534, 'Socks', 'Quiksilver', 12.0, 2),
    (9423679, 'T-shirt', 'Patagonia', 35.0, 1),
    (4626377, 'Hoody', 'Animal', 44.0, 1),
    (4626377, 'Cargo Shorts', 'Animal', 38.0, 1),
    (4626412, 'Shirt', 'Volcom', 78.0, 1),
    (9423783, 'Boxer Shorts', 'Superdry', 30.0, 2),
    (9423783, 'Shorts', 'Globe', 26.0, 1),
    (4626490, 'Cargo Shorts', 'Billabong', 54.0, 1),
    (4626490, 'Sweater', 'Dickies', 56.0, 1),
]
df_details = pd.DataFrame(details, columns=['OrderNo', 'Item', 'Brand', 'Price', 'Quantity'])

emps = [
    (9001, 'Jeff', 'LA'),
    (9002, 'Jane', 'San Fran'),
    (9003, 'Tom', 'NYC'),
    (9004, 'Maya', 'Philadelphia')
]
df_emps = pd.DataFrame(emps, columns=['Empno', 'Empname', 'Location'])

locations = [
    ('LA', 'West'),
    ('San Fran', 'West'),
    ('NYC', 'East'),
    ('Philadelphia', 'East'),
]
df_locations = pd.DataFrame(locations, columns=['Location', 'Region'])

df_sales = df_orders.merge(df_details)
df_sales['Total'] = df_sales['Price'] * df_sales['Quantity']  # Add new 'Total' column
df_sales = df_sales[['Date', 'Empno', 'Total']]  # Only show these 3 columns
df_sales_emps = df_sales.merge(df_emps)
df_results = df_sales_emps.merge(df_locations)
df_results = df_results[['Date', 'Region', 'Total']]  # Only show these 3 columns
df_date_region = df_results.groupby(['Date', 'Region']).sum()  # 'Total' not specified as it's the only numerical column
# print(df_results)
# print(df_date_region)
# print(df_date_region.index)
# print(df_date_region[df_date_region.index.isin([('2022-02-05', 'West')])])  # Show the row which corresponds to this date and region
# print(df_date_region[df_date_region.index.isin([('2022-02-05', 'East'), ('2022-02-05', 'West')])])  # Multiple of the above
# print(df_date_region[('2022-02-04', 'East'):('2022-02-05', 'West')])  # Slicing a range of aggregate values
# print(df_date_region['2022-02-04':'2022-02-05'])  # Same as the above, omitted regions as it all regions that are required
# print(df_date_region.loc[(slice('2022-02-05', '2022-02-06'), slice(None)), :])  # Slicing aggregation levels based on level of aggregation order = Date, Region
# print(df_date_region.loc[(slice('2022-02-05', '2022-02-06'), slice('East')), :])  # As above but selecting 'East'
ps = df_date_region.sum(axis=0)  # Adding a grand total, 'Total' not required as it's the only numerical data in this dataframe
ps.name = ('All', 'All')  # Give this data series a name
# print(ps)
df_date_region_total = df_date_region.append(ps)  # Append series to dataframe
# print(df_date_region_total)
# print(df_date_region_total[df_date_region_total.index.isin([('All', 'All')])])  # Show only the total using .index.isin()

#  Adding a subtotal
df_totals = pd.DataFrame()
for date, date_df in df_date_region.groupby(level = 0):
    df_totals = df_totals.append(date_df)
    ps = date_df.sum(axis = 0)
    ps.name = (date, 'All')
    df_totals = df_totals.append(ps)
df_totals = df_totals.append(df_date_region_total.loc[('All', 'All')])
# print(df_totals)

group = df_results.groupby(['Date', 'Region'])  # Selecting all rows in a group
print(group.get_group(('2022-02-04', 'West')))
