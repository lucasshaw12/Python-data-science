#! python3
# Gaining insight from data
# Analysing and visualising data to make decisions and conclusions = market basket analysis
# mlxtend library and Apriori algorithm

##############
# Apriori algorithm - analysing transaction data
##############

import pandas as pd
from mlxtend.preprocessing import TransactionEncoder

transactions = [
    ['curd', 'sour cream'], ['curd', 'orange', 'sour cream'],
    ['bread', 'cheese', 'butter'], ['bread', 'butter'],
    ['bread', 'milk'], ['apple', 'orange', 'pear'], ['bread', 'milk', 'eggs'],
    ['tea', 'lemon'], ['curd', 'sour cream', 'apple'], ['eggs', 'wheat flour', 'milk'],
    ['pasta', 'cheese'], ['bread', 'cheese'], ['pasta', 'olive oil', 'cheese'],
    ['curd', 'jam'], ['bread', 'cheese', 'butter'], ['bread', 'sour cream', 'butter'],
    ['strawberry', 'sour cream'], ['curd', 'sour cream'], ['bread', 'coffee'],
    ['onion', 'garlic']
]
encoder = TransactionEncoder()
encoded_array = encoder.fit(transactions).transform(transactions)
df_itemsets = pd.DataFrame(encoded_array, columns=encoder.columns_)
# print(df_itemsets)
# print('Number of transactions: ', len(transactions))
# print('Number of unique items: ', len(set(sum(transactions, []))))

##############
# identifying frequent itemsets
##############
from mlxtend.frequent_patterns import apriori, association_rules
frequent_itemsets = apriori(df_itemsets, min_support=0.1, use_colnames=True)  # identify all the frequent itemsets with 10% support
# print(frequent_itemsets)
frequent_itemsets['length'] = frequent_itemsets['itemsets'].apply(lambda itemset: len(itemset))  # Only view itemsets with multiple items
# print(frequent_itemsets[frequent_itemsets['length'] >= 2])  # Only view itemsets with multiple items

##############
# Generating association rules
##############
rules = association_rules(frequent_itemsets, metric='confidence', min_threshold=0.5)  # generate association rules for itemsets
# print(rules.iloc[:,0:7])

##############
# Visualising association rules
##############
rules_plot = pd.DataFrame()
rules_plot['antecedents'] = rules['antecedents'].apply(lambda x: ','.join(list(x)))
rules_plot['consequents'] = rules['consequents'].apply(lambda x: ','.join(list(x)))
rules_plot['lift'] = rules['lift'].apply(lambda x: round(x, 2))
pivot = rules_plot.pivot(index='antecedents', columns='consequents', values='lift')
# print(pivot)
antecedents = list(pivot.index.values)  # assign the df index names list to a variable
consequents = list(pivot.columns)  # assign the df column names list to a variable
pivot = pivot.to_numpy()  # assign plot values to numPy array
# print(pivot)

##############
# Build a heatmap using the above
##############
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots()
im = ax.imshow(pivot, cmap='Reds')  # convert pivot array data to colour coded 2D image
ax.set_xticks(np.arange(len(consequents)))
ax.set_yticks(np.arange(len(antecedents)))
ax.set_xticklabels(consequents)
ax.set_yticklabels(antecedents)
plt.setp(ax.get_xticklabels(), rotation=45, ha='right', rotation_mode='anchor')
for i in range(len(antecedents)):
    for j in range(len(consequents)):
        if not np.isnan(pivot[i, j]):
            text = ax.text(j, i, pivot[i, j], ha='center', va='center')
ax.set_title('Lift metric for frequent itemsets')
fig.tight_layout()
# plt.show()

##############
# Gain actionable insights from association rules - generating recommendations
##############
butter_antecedent = rules[rules['antecedents'] == {'butter'}][['consequents', 'confidence']].sort_values('confidence', ascending=False)
butter_consequents = [list(item) for item in butter_antecedent.iloc[0:3,]['consequents']]  # extract top 3 consequents
item = 'butter'
# print('items bought frequently with', item, 'are: ', butter_consequents)

##############
# Planning discounts based on association rules
##############

from functools import reduce
rules['itemsets'] = rules[['antecedents', 'consequents']].apply(lambda x: reduce(frozenset.union, x), axis=1)
# print(rules[['antecedents', 'consequents', 'itemsets']])
rules.drop_duplicates(subset=['itemsets'], keep='first', inplace=True)
# print(rules[['itemsets']])
discounted = []
others = []
for itemset in rules['itemsets']:
    for i, item in enumerate(itemset):
        if item not in others:
            discounted.append(item)
            itemset = set(itemset)
            itemset.discard(item)
            others.extend(itemset)
            break
        if i == len(itemset)-1:
            discounted.append(item)
            itemset = set(itemset)
            itemset.discard(item)
            others.extend(itemset)
print(discounted)
print(list(set(discounted)))  # show discounted items without duplicates





















