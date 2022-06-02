def linear_search_dictionary(my_dictionary, value):
    if value in my_dictionary.values():
        key = [ k for k, v in my_dictionary.items() if v == value]
        print("Found at key", key)
        return
    else:
        print("Target is not in the dictionary")
        return -1

my_dictionary = {"red": 5, "blue": 3, "yellow": 12, "green": 7}
linear_search_dictionary(my_dictionary, 5)
linear_search_dictionary(my_dictionary, 3)
linear_search_dictionary(my_dictionary, 8)


