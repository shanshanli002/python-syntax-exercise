def print_upper_words(list_of_words, must_start_with):
    """function takes in a list of words and prints all elements starting with keys in must_start_with & in uppercase"""
    for word in list_of_words: 
        #if word[0] == 'e':
        #    print(word.upper())
        if word[0] in must_start_with:
            print(word.upper())

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], must_start_with = {"h", "y"})