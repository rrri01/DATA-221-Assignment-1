from random import random

values = [random() for i in range(20)]
x = random()

values.sort() # this will make python re-order the list of values

values_greater_than_or_equal_to_x = []
for value in values:
    if value >= x:
        values_greater_than_or_equal_to_x.append(value)

print(values) # this will print the sorted list because we used .sort() earlier
print(x)


# here is to check if there are any values in our list that match x, and tell us the index of that value
first_matching_value_index = 0
for value in values:
# just because we are using floats, it is very unlikely that our x will match a value in the list
    if value == x:
        print(first_matching_value_index)
        break
    first_matching_value_index += 1


