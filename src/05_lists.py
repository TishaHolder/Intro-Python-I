# For the exercise, look up the methods and functions that are available for use
# with Python lists.

"""lists or dictionaries are passed by reference. everything else is passed by value"""

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE
x.append(4)
print("x after append:", x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE
x.extend(y)
print("x after extend:", x)

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE
x.pop(4)
print("x after pop:", x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE
x.insert(5, 99)
print("x after insert:", x)

# Print the length of list x
# YOUR CODE HERE
print ("the length of the list x:", len(x))

# Print all the values in x multiplied by 1000
# YOUR CODE HERE
print ([value * 1000 for value in x])

"""
we have two ways of iterating through a list.

Method 1 - for item in list:

for item in list:
  print item
Method 2 - iterate through indexes:

for i in range(len(list)):
  print list[i]
Method 1 is useful to loop through the list, but it’s not possible to modify the list this way.

Method 2 uses indexes to loop through the list, making it possible to also modify the list if needed. 

Lists of lists
list_of_lists = [[1, 2, 3], [4, 5, 6]]

for lst in list_of_lists:
  for item in lst:
    print item

"""