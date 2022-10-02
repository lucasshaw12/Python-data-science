#! python3

# Python dictionary data structure exercises.

##############
# Counting number of occurrences within a text phrase using a dictionary
##############

txt = '''python is one of the most promising programming languages today. Due to the simplicity of the python syntax,
            many researches and scientists prefer python over many other languages.'''

# Replace punctuation with '' (space)
txt = txt.replace(',', '').replace('.', '')
lst = txt.split()
print(lst)

#  Count the occurrences
dct = {}
for w in lst:
    c = dct.setdefault(w, 0)
    dct[w] += 1
dct_sorted = dict(sorted(dct.items(), key=lambda x: x[1], reverse=True))
# print(dct_sorted)
