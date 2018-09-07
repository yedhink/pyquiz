'''
A tuple is a collection which is ordered and unchangeable. In Python tuples are written with
round brackets.
The Tuples have following properties:
- You cannot change values in a tuple.
- You cannot remove items in a tuple.
'''

# note the comma
singleton_tuple = 1,

# this is the proper way to intialize a tuple
t1 = (1, 2, 3, 1)

# most methods that can be applied on lists,strings and other sequences
# can be applied with tuples
print(len(t1))
print(t1.count(1))

'''
when to prefer tuples over lists??
- tuples have faster iteration than lists
- non-changebale values..say the location co_ordinates should be stored in a tuple
'''

# The following example is called tuple packing:
co_ordinates = 76.88, 96.99

# The following example is called tuple unpacking:
longitude, latitude = co_ordinates

print("Currently im at {}:{}".format(longitude, latitude))

'''
This is called, appropriately enough, sequence unpacking and
works for any sequence on the
right-hand side. Sequence unpacking requires that there are
as many variables on the left
side of the equals sign as there are elements in the sequence.
Note that multiple assignment is really just a combination of
tuple packing and sequence unpacking.
'''
# Q) write the python code to swap two variables
name1 = "name1"
name2 = "name2"
