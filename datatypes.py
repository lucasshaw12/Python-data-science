#! python3
# Using datatypes - lists, sets, dictionary


##################################
############## LISTS ##############
##################################
##############
# List Queues
##############
# my_list = ['Pay bills', 'Tidy up', 'walk the dog', 'go to pharmacy', 'cook dinner']
#
# from collections import deque
# queue = deque(my_list)
# queue.append('wash the car')
# print(queue.popleft(), ' - Done.')  # Removes then returns the  leftmost item within the list 'Pay bills'
# print(queue)

##############
# List stacks
##############

# my_list = ['Pay bills', 'Tidy up', 'walk the dog', 'go to pharmacy', 'cook dinner']
# stack = []
# for task in my_list:
#     stack.append(task)
# while stack:
#     print(stack.pop(), ' - Done.')  # Removes then returns the last item added to the list
# print('\n the stack is empty')
# print(stack)

##############
# List comprehensions
##############

# txt = '''Eight dollars a week or a million a year - whats the difference? A mathematician or a wit would give you
# the wrong answer. The magi brought valuable gifts, but that was not among them. - The gift of maji O'Henry.'''
#
# word_lists = [[w.replace(',' , '') for w in line.split() if w not in ['-']] for line in txt.replace('?',
# '.').split('.')]
# print(word_lists)

##############
# List & stacks for natural language processing
##############

# import spacy
# txt = 'List is a ubiquitous data structure in the Python programming language.'
# nlp = spacy.load('en_core_web_sm')
# doc = nlp(txt)
# stk = []
# for w in doc:
#     if w.pos_ == 'NOUN' or w.pos_ == 'PROPN':
#         stk.append(w.text)
#     elif (w.head.pos_ == 'NOUN' or w.head.pos_ == 'PROPN') and (w in w.head.lefts):
#         stk.append(w.text)
#     elif stk:
#         chunk = ''
#         while stk:
#             chunk = stk.pop() + ' ' + chunk
#         print(chunk.strip())


##############
# List comprehensions for natural language processing
##############

# import spacy
# txt = 'List is arguably the most useful type in the python programming language.'
# nlp = spacy.load('en_core_web_sm')
# doc = nlp(txt)
# stk = []
# for w in doc:
#     head_lefts = [1 if t in t.head.lefts else 0 for t in doc[w.i:]]
#     i0 = 0
#     try: i0 = head_lefts.index(0)
#     except ValueError: pass
#     i1 = 0
#     if i0 > 0:
#         noun = [1 if t.pos_ =='NOUN' or t.pos_ == 'PROPN' else 0 for t in reversed(doc[w.i:w.i+i0 +1])]
#         try: i1 = noun.index(1)+1
#         except ValueError: pass
#     if w.pos_ == 'NOUN' or w.pos_ == 'PROPN':
#         stk.append(w.text)
#     elif (i1 > 0):
#         stk.append(w.text)
#     elif stk:
#         chunk = ''
#         while stk:
#             chunk = stk.pop() + ' ' + chunk
#         print(chunk.strip())
#
# task_list = ['pay bills', 'tidy up', 'walk the dog', 'go to pharmacy', 'cook dinner']
# task_tm = ['8:00', '8:30', '9:00', '10:00', '10:30']
#
# sched_list = [(tm, task) for tm, task in zip(task_tm, task_list)]
# print(type(sched_list))
# print(sched_list[1][0])
# print(sched_list[1][1])

##################################
############## SETS ##############
##################################

##############
# Removing duplicates from sets
##############

# lst = ['john silver', 'tim jemison', 'john silver', 'maya smith']
# lst = list(set(lst))
# print(lst)

##############
# Set intersections - combining similarities in elements of sets
##############

# photo1_tags = {'coffee', 'table', 'drinks', 'breakfast', 'tableware', 'cup', 'food'}
# photo2_tags = {'food', 'dish', 'meat', 'meal', 'tableware', 'dinner', 'vegetable'}
#
# intersection = photo1_tags.intersection(photo2_tags)
# if len(intersection) >= 2:
#     print('These tags are common ', intersection)

########################################
############## DICTIONARY ##############
########################################

##############
# Counting number of occurrences within a text phrase using a dictionary
##############

# txt = '''python is one of the most promising programming languages today. Due to the simplicity of the python syntax,
#             many researches and scientists prefer python over many other languages.'''
#
# # Replace punctuation with '' (space)
# txt = txt.replace(',', '').replace('.', '')
# lst = txt.split()
# print(lst)
#
# #  Count the occurrences
# dct = {}
# for w in lst:
#     c = dct.setdefault(w, 0)
#     dct[w] += 1
# dct_sorted = dict(sorted(dct.items(), key=lambda x: x[1], reverse=True))
# print(dct_sorted)
