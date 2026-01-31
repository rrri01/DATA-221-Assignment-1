def nested_dictionary_from_strings(list_of_strings):
    dictionary_of_words = {} # create an empty dictionary which we will add to later
    for string in list_of_strings:
        length_of_string = len(string) # get the length of each string in the list
        if length_of_string % 2 == 0: # find out if there is an odd or even amount of letters
            parity = "even"
        elif length_of_string % 2 == 1:
            parity = "odd"
        dictionary_of_words[string] = {"length": length_of_string, "parity": parity}

    return dictionary_of_words

print(nested_dictionary_from_strings(["data", "science"])) # print and call the function

