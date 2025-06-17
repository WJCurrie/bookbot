#this is intended to be a guided project for a python
#program that searches for book text(I think?) As I am 
#fairly sure that my VSCode and so on is not set up correctly,
#I'm not sure this will ever work as expected.

#importing stuff
from stats import word_num, get_book_text, char_count

#create 'main' function here to run the program
def main():
    num_char = {}
    #string creation to direct to the file
    bookplace = "/home/whitn/bookbot/books/frankenstein.txt"
    #string to hold the txt from the file
    booktxt = (get_book_text(bookplace))
    #int to hold the number of words
    word_count = (word_num(booktxt))
    #number of times per char
    num_char = (char_count(booktxt))
    
    print(num_char)
    
    #removed per instructions
    #print(word_count, 'words found in the document')

    #removed per instructions
    #print(booktxt)

    #close out
    exit()

    
#call main function to kick off everything
main()