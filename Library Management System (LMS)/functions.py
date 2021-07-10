from book import book
import json

# Print function

def print_options():
    print("Please select the option from below list.")
    print("Press 1 to create a new book")
    print("Press 2 to save books locally")
    print("Press 3 to load books from the disk")
    print("Press 4 for issuance of book")
    print("Press 5 to return a book")
    print("Press 6 to update a book")
    print("Press 7 to show all books")
    print("Press 8 to show book")


# Book info function

def input_book_info():
    id = input("ID: ")
    name = input("Name: ")
    description = input("Description: ")
    isbn = input("ISBN: ")
    page_count = int(input("Page Count: "))
    issued = input("Issued: y/Y for True, anything else for False: ")
    issued = (issued =="y" or issued == "Y")
    author = input("Author Name: ")
    year = int(input("Year: "))
    return{
        "id": id,
        "name":name,
        "description":description,
        "isbn":isbn,
        "page_count":page_count,
        "issued":issued,
        "author":author,
        "year":year
    }

# Creat a book function

def create_book():
    print("Please enter your book information")
    book_input = input_book_info()
    my_book = book(book_input["id"], book_input["name"], book_input["description"], book_input["isbn"], 
              book_input["page_count"], book_input["issued"], book_input["author"], book_input["year"])  
    print(my_book.to_dict())
    return my_book

# Save books function

def save_books(books):
    json_books = []
    for my_book in books:
        json_books.append(my_book.to_dict())
    try:
        file = open("books.data","w")
        file.write(json.dumps(json_books, indent=4))
    except:
        print("We had an error savings books")
    
