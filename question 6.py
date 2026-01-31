
def distribution_analysis(numbers):
    dictionary_of_values = {}
    unique_keys = set() # set will re order the numbers and ignore any duplicates for us
    for number in numbers:
        unique_keys.add(number)

    for key in unique_keys:
        # adds each key to the dictionary and set the value as 0 for now
        dictionary_of_values[key] = 0

    for number in numbers:  # updates how many times each number appears
        dictionary_of_values[number] += 1

    return dictionary_of_values


# call the function and print the result
print(distribution_analysis([3, 1, 2, 3, 4, 2]))
