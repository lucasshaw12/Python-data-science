#! python3

# Python sets data structure exercises.
# Unordered allocation of items

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

l = [
 {
  "name": "photo1.jpg",
  "tags": {'coffee', 'breakfast', 'drink', 'table', 'tableware', 'cup', 'food'}
 },
 {
  "name": "photo2.jpg",
  "tags": {'food', 'dish', 'meat', 'meal', 'tableware', 'dinner', 'vegetable'}
 },
 {
  "name": "photo3.jpg",
  "tags": {'city', 'skyline', 'cityscape', 'skyscraper', 'architecture', 'building', 'travel'}
 },
 {
  "name": "photo4.jpg",
  "tags": {'drink', 'juice', 'glass', 'meal', 'fruit', 'food', 'grapes'}
 }
]

photo_groups = {}
for i in range(1, len(l)):
    for j in range(i+1, len(l)+i):
        tags = l[i]['tags']
        c = photo_groups.setdefault('tags', 0)
        photo_groups[c] += 1
        print(photo_groups)

        # tags = l[i]['tags']
        # tags_2 = l[j]['tags']
        # c = photo_groups.setdefault(i, 0)
        # photo_groups[i] += 1
        # intersection = tags.intersection(tags_2)
        # print(tags)
        # print(tags_2)