def exponent_function(list_of_pairs):
    list_of_final_values = [] # empty list that we will add some values to later
    for pair in list_of_pairs: # this loop cycles through each list nested in the main list
        x = pair[0] # x will be the first number in this pair
        y = pair[1] # y will be the second number in this pair

        if y >= 0: # if y is positive (or 0)
            list_of_final_values.append(x**y)

    print(list_of_final_values)


pairs = [[5, 2], [3, -1], [4, 3], [2, 0]]
exponent_function(pairs) # call the function

