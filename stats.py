#start by defining the get book text function
def get_book_text(bookfile):
    with open(bookfile) as f:
        filling = f.read()
    return filling

def word_num(contents):
     #so a note here. This is creating a list of the words from the file,
     #then returning the total length of the list. I did attempt a loop,
     #but this book is exceptionally long, and the look was taking too much time.
     bwords = contents.split()
     return len(bwords)

def char_count(contents):
    #build the dictionary and lower all cases in the given string
    char_dict = {}

    l_contents = contents.lower()

    for letter in l_contents:
        if letter in char_dict:
            char_dict[letter] += 1
        else:
            char_dict[letter] = 1

    #hopefully just need to return the dictionary
    return char_dict