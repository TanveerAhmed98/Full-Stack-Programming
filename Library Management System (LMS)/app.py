import functions
import os

functions.print_options()
option = input()
books = []
while option != "x" and option != "X":
    if option == "1" :
        books.append(functions.create_book())
        input("Command executed ... Press any button to continue: ")
    elif option == "2":
        functions.save_books(books)
    option = input()
    
