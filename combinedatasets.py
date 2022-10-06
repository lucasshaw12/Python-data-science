#! python3
# Combining datasets

###########################
# Combining Lists and Tuples with +
###########################

orders_2022_02_04 = [
    (9423517, '2022-02-04', 9001),
    (4626232, '2022-02-04', 9003),
    (9423534, '2022-02-04', 9001)
]

orders_2022_02_05 = [
    (9423679, '2022-02-05', 9002),
    (4626377, '2022-02-05', 9003),
    (9423534, '2022-02-05', 9003)
]

orders_2022_02_06 = [
    (9423783, '2022-02-06', 9004),
    (4626490, '2022-02-06', 9004)
]

orders = orders_2022_02_04 + orders_2022_02_05 + orders_2022_02_06
# print(orders)


###########################
# Combining Dictionaries with **
###########################

extra_fields_9423517 = {
    'ShippingInstructions': {
        'name': 'john silver',
        'Phone': [{'type': 'Office', 'number': '809-123-9309'},
                  {'type': 'mobile', 'number': '417-123-4567'}
                  ]
    }
}

order_9423517 = {'OrderNo': 9423517, 'Date': '2022-02-04', 'Empno': 9001}
order_9423517 = {**extra_fields_9423517, **order_9423517}
# print(order_9423517)

###########################
# Combining corresponding rows 2 structures
###########################

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
    (4626490, 'Sweater', 'Dickies', 56.0, 1)
]

orders_details = []
for o in orders:
    for d in details:
        if d[0] == o[0]:
            orders_details.append(o + d[1:])
# print(orders_details)

###########################
# Concatenating NumPy arrays
###########################

# Creating Numpy array
import numpy as np

jeff_salary = [2700, 3000, 3000]
nick_salary = [2600, 2800, 2800]
tom_salary = [2300, 2500, 2500]
base_salary1 = np.array([jeff_salary, nick_salary, tom_salary])
maya_salary = [2200, 2400, 2400]
john_salary = [2500, 2700, 2700]
base_salary2 = np.array([maya_salary, john_salary])
base_salary = np.concatenate((base_salary1, base_salary2), axis=0)  # Combine salaries
# print(base_salary)
new_month_salary = np.array([[3000], [2900], [2500], [2500], [2700]])
# print(new_month_salary)
base_salary = np.concatenate((base_salary, new_month_salary), axis=1)
# print(base_salary)

###########################
# Concatenating Pandas DataFrames
###########################

import pandas as pd

salary_df1 = pd.DataFrame(
    {'jeff': jeff_salary,
     'nick': nick_salary,
     'tom': tom_salary
     }
)
salary_df1.index = ['June', 'July', 'August']  # Add this index to the DF
salary_df1 = salary_df1.T
# print(salary_df1)
salary_df2 = pd.DataFrame(
    {'maya': maya_salary,
     'john': john_salary
     },
    index=['June', 'July', 'August']
).T
salary_df = pd.concat([salary_df1, salary_df2])  # Concatenate DF's
# print(salary_df)
salary_df3 = pd.DataFrame(
    {'September': [3000, 2800, 2500, 2400, 2700],
     'October': [3200, 3000, 2700, 2500, 2900]
     },
    index=['jeff', 'nick', 'tom', 'maya', 'john']
)
salary_df = pd.concat([salary_df, salary_df3], axis=1)  # Concatenate/add new columns
# print(salary_df)
salary_df = salary_df.drop(['September', 'October'], axis=1)  # Remove columns
# print(salary_df)
salary_df = salary_df.drop(['nick', 'maya'], axis=0)  # Remove rows
# print(salary_df)

###########################
# Concatenating Pandas DataFrames with hierarchical Index
###########################

df_date_region1 = pd.DataFrame(
    [
        ('2022-02-04', 'East', 97.0),
        ('2022-02-04', 'West', 243.0),
        ('2022-02-05', 'East', 160.0),
        ('2022-02-05', 'West', 35.0),
        ('2022-02-06', 'East', 110.0),
        ('2022-02-06', 'West', 860.0),
    ],
    columns=['Date', 'Region', 'Total']).set_index(['Date', 'Region'])

df_date_region2 = pd.DataFrame(
    [
        ('2022-02-04', 'South', 114.0),
        ('2022-02-05', 'South', 325.0),
        ('2022-02-06', 'South', 212.0)
    ],
    columns=['Date', 'Region', 'Total']).set_index(['Date', 'Region'])

df_date_region = pd.concat([df_date_region1, df_date_region2]).sort_index(level=['Date', 'Region'])  # Keep it sorted by date rather than
# ...appending the 2nd DF to the end.
# print(df_date_region)

###########################
# Concatenating Pandas DataFrames right-join
###########################
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
df_orders = pd.DataFrame(orders, columns=['OrderNo', 'Date', 'Empno'])
df_details = pd.DataFrame(details, columns=['OrderNo', 'Item', 'Price', 'Brand', 'Quantity'])

df_details = df_details.append(
    {
        'OrderNo': 4626592,
        'Item': 'Shorts',
        'Brand': 'Protest',
        'Price': 48.0,
        'Quantity': 1
    },
    ignore_index=True
)
df_orders_details_right = df_orders.merge(df_details, how='right', left_on='OrderNo', right_on='OrderNo')
# print(df_orders_details_right)
# print(df_orders_details_right.dtypes)  # Shows that 'EmpNo' have been converted to 'float64' from 'int64' due to 'NaN' value
df_orders_details_right = df_orders_details_right.fillna({'Empno': 0}).astype({'Empno': 'int64'})  # Ensure 'EmpNo'...
# ...returns to a 'int' value of '0' rather than a 'float
# print(df_orders_details_right)
# print(df_orders_details_right.dtypes)


###########################
# Concatenating Pandas DataFrames many-to-many join
###########################

books = pd.DataFrame(
    {
        'book_id': ['b1', 'b2', 'b3'],
        'title': ['Beautifiul coding', 'Python for web development', 'Pythonic thinking'],
        'topic': ['programming', 'Python, web', 'Python']
    }
)
authors = pd.DataFrame(
    {
        'author_id': ['jsn', 'tri', 'wsn'],
        'author': ['Johnson', 'Treloni', 'Wilson']
    }
)
#  Create 3rd DF as associate to combine the 'author' and 'book' DF. Needs one-to-many with all other DF's
matching = pd.DataFrame(
    {
        'author_id': ['jsn', 'jsn', 'tri', 'wsn'],
        'book_id': ['b1', 'b2', 'b2', 'b3']
    }
)
# print(matching)
authorship = books.merge(matching).merge(authors)[['title', 'topic', 'author']]  # Merge 'books' with 'matching'...
# ...then merge to 'authors'.
print(authorship)


































