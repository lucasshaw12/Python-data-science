#! python3

# Data science modules = numpy, pandas, scikit-learn
import json
import pandas as pd
import numpy as np

##############
# NUMPY
##############

# Creating Numpy array
# jeff_salary = [2700, 3000, 3000]
# nick_salary = [2600, 2800, 2800]
# tom_salary = [2300, 250, 2500]
# base_salary = np.array([jeff_salary, nick_salary, tom_salary])
# print(base_salary)
#
# jeff_bonus = [500, 400, 400]
# nick_bonus = [600, 300, 400]
# tom_bonus = [200, 500, 400]
# bonus = np.array([jeff_bonus, nick_bonus, tom_bonus])
#
# salary_bonus = base_salary + bonus
# print(type(salary_bonus))
# print(salary_bonus)
# print(salary_bonus.max())  # Print maximum value within array
# print(np.amax(salary_bonus, axis =1))  # Search across the columns then print maximum value from last 3 months
# print(np.average(salary_bonus, axis =1))  # Search across the columns then print average value
# print(np.amax(salary_bonus, axis =0))  # Search across the columns then print maximum value a month

##########################################
# PANDAS
##########################################
# Creating dataframe
# data = ['Jeff', 'Jane', 'Tom']
# emps_names = pd.Series(data)
# print(emps_names)
#
##############
# # Accessing dataframe
##############
# emps_names = pd.Series(data, index=[9001, 9002, 9003])
# print(emps_names)
# print(emps_names[9001])
# print(emps_names.loc[9001])  # use index to find element
# print(emps_names.iloc[0])  # Use integar-index to find element
# print(emps_names.loc[9001:9002])  # Use integar-index to find element
#
##############
# # Combining multiple Series into a dataframe
##############
# data = ['jeff', 'jane', 'tom']
# nums = ['234567', '7843285943', '98345947835']
# emps_phones = pd.Series(nums, index=[9001, 9002, 9003], name='numbers')
# emps_emails = pd.Series(data, index=[9001, 9002, 9003], name='emails')
# emps_names.name = 'names'
# df = pd.concat([emps_names, emps_emails, emps_phones], axis=1)
# print(df)

##############
# Creating Pandas dataframe using API data = yfinance
##############
# import yfinance as yf
# tkr = yf.Ticker('TSLA')
# hist = tkr.history(period='5d')
# hist = hist.drop("Dividends", axis = 1)
# hist = hist.drop('Stock Splits', axis = 1)
# hist = hist.reset_index()
# hist = hist.set_index('Date')
# print(hist)

##############
# Converting JSON to Pandas dataframe
#############
# data = [
#     {'Empno':9001, 'Salary': 3000},
#     {'Empno':9002, 'Salary': 2800},
#     {'Empno':9003, 'Salary': 2500},
#     {'Empno':9005, 'Salary': 4000}
# ]
# json_data = json.dumps(data)
# salary = pd.read_json(json_data)
# salary = salary.set_index('Empno')
# # print(salary)
#
# ##############
# # Create dataframe from list of lists
# ##############
# data = [['9001', 'jeff', 'sales'],
#         ['9002', 'jane', 'sales'],
#         ['9003', 'tom', 'sales']]
# emps = pd.DataFrame(data, columns=['Empno', 'Name', 'Job'])
# column_types = {'Empno': int, 'Name':str, 'Job': str}
# emps = emps.astype(column_types)
# emps = emps.set_index('Empno')
# # print(emps)
#
# ##############
# # Combining dataframes
# ##############
#
# emps_salary = emps.join(salary)
# # print(emps_salary)
# new_emp = pd.Series({'Name': 'john', 'Job':'sales'}, name=9004) #  Adding new df which has rows with no matches to other df
# emps = emps.append(new_emp)
# # print(emps)
# emps_salary = emps.join(salary)
# # print(emps_salary)
#
# emps_salary = emps.join(salary, how='inner')  # 'inner' shows only the intersection of the combined df's
# # print(emps_salary)
#
# ##############
# # One to many joins
# ##############
#
# data=[[2608, 9001,35], [2617, 9001,35], [2620, 9001, 139], [2621, 9002,95], [2626, 9002,218]]
# orders = pd.DataFrame(data, columns=['Pono', 'Empno', 'Total'])
# print(orders)
# emps_orders = emps.merge(orders, how='inner', left_on='Empno', right_on='Empno').set_index('Pono')
# print(emps_orders)
#
# ##############
# # Aggregating data with group-by
# ##############
#
# print(orders.groupby(['Empno'])['Total'].mean())
# print(orders.groupby(['Empno'])['Total'].sum())

##############
# Scikit-learn (used for machine learning)
##############
# from sklearn.model_selection import train_test_split
# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.linear_model import LogisticRegression
# df = pd.read_csv('amazon_cells_labelled.txt', names=['reviews', 'sentiment'], sep='\t')
# reviews =df['reviews'].values
# sentiments = df['sentiment'].values
# reviews_train, reviews_test, sentiment_train, sentiment_test = train_test_split(reviews, sentiments, test_size=0.2, random_state=500)
# vectoriser = CountVectorizer()
# vectoriser.fit(reviews)
# X_train = vectoriser.transform(reviews_train)
# X_test = vectoriser.transform(reviews_test)
# classifier = LogisticRegression()
# classifier.fit(X_train, sentiment_train)
# accuracy = classifier.score(X_test, sentiment_test)
# print('Accuracy:', accuracy)
#
# new_reviews = ['Old version of python is useless', 'very good effort,  but not five stars', 'Clear and concise']
# X_new = vectoriser.transform(new_reviews)
# print(classifier.predict(X_new))







