#this is intended to be a guided project for a python
#program that searches for book text(I think?) As I am 
#fairly sure that my VSCode and so on is not set up correctly,
#I'm not sure this will ever work as expected.

#importing stuff
from stats import word_num, get_book_text, char_count, sortdict

#create 'main' function here to run the program
def main():
    #creating dictionaries
    num_char = {}
    sortchar = []
    #string creation to direct to the file
    bookplace = "/home/whitn/bookbot/books/frankenstein.txt"
    #string to hold the txt from the file
    booktxt = (get_book_text(bookplace))
    #int to hold the number of words
    word_count = (word_num(booktxt))
    #number of times per char
    num_char = (char_count(booktxt))
    #sorting dictionary and so on
    sortchar = (sortdict(num_char))

    #attempting to generate report
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print("Found", word_count, "total words")
    print("--------- Character Count -------")
    
    for item in sortchar:
        character = item["letter"]
        count = item["num"]
        if character.isalpha():
            print(f"{character}: {count}")

    print("============= END ===============")

    #close out
    exit()

    
#call main function to kick off everything
main()