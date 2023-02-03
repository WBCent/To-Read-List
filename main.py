reading_list = []
list_options = """Please enter one of the following choices:

- 'b' to add a book
- 'l' to list all books
- 'q' to quit
"""

user_input = input(list_options)




if(user_input == 'b'):
    book_title = input("Please enter book title")
    reading_list.append(book_title)
    print("added to reading list")
elif(user_input == 'l'):
    print(reading_list)
elif(user_input == 'q'):
    quit()


user_input = input(list_options)