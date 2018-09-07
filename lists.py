'''
Python knows a number of compound data types, used to group together
other values. The most versatile is the list, which can be written as a
list of comma-separated values (items) between square brackets. Lists
might contain items of different types, but usually the items all have
the same type.

NOTE : not all methods has been mentioned here. do google the rest and find out
'''

my_list = [3, 2, 1, 4, 5]
# indexing: 0  1  2  3  4
#reverse :-5 -4 -3  -2 -1
# accessing values
# print(my_list[-5])
# same reverse indexing for strings


# It is possible to nest lists (create lists containing other lists),
# for example:
list_of_chars = ['a', 'b', 'c']
list_of_numbers = [1, 2, 3]
mixed_list = list_of_chars

# extend concatenates the first list with another list
# (or another iterable, not necessarily a list.)
mixed_list.extend(list_of_numbers)

# to find lenght of list use len()
#print("our list initially = {}".format(mixed_list))

# to add a value to end of the list
mixed_list.append(1)

# Remove the first item from the list whose value is equal to x.
# It raises a ValueError if there is no such item.
mixed_list.remove('a')

# Insert an item at a given position. The first argument is the index of the element
# before which to insert, so a.insert(0, x) inserts at the front of the list,
# and a.insert(len(a), x) is equivalent to a.append(x).
mixed_list.insert(0, 'first')

# list.index(x[, start[, end]])
# Return zero-based index in the list of the first item whose value is equal to x.
mixed_list.index(3)

# list.count(x)
# Return the number of times x appears in the list.
mixed_list.count(1)


# SLICING
# a[start:end:step] # start through not past end, increasing by step
# y e d h i n
# 0 1 2 3 4 5
name = "yedhin"
# print(name[0:6:2])
# print(name[-2:-1])

# replacing values using slicing
mixed_list[:] = [1, 2, 3]

print("our list after replacing = {}".format(mixed_list))
# Q) replace the last 3 chars with a,b,c
