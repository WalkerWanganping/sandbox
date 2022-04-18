"""
Replace the contents of this module docstring with your own details
Name:Wang Anping
Date started:13/4/22
GitHub URL:https://github.com/WalkerWanganping
"""
import csv
FILE_DIRECTORY = "books.csv"
REQUIRED = "r"
COMPLETED = "c"
MENU = f"Menu:\n L - List all books\n A - Add new book\n M - Mark a book as completed\n Q - Quit\nenter your choice:"


def load_books():
    """Load book details from file into list."""
    book_file = open(FILE_DIRECTORY, "r")
    books = []
    for line in book_file:
        line = line.strip()
        parts = line.split(',')
        parts[-2] = int(parts[-2])
        books.append(parts)
    book_file.close()
    print(f"{len(books)} books loaded")
    return books

def main():
    """display main menu"""
    print("Reading Tracker 1.0 - by Wang Anping")
    books = load_books()

    user_choice = input(MENU).upper().strip()
    while user_choice != "Q":
        if user_choice == "L":
            list_all_books(books)

        elif user_choice == "A":
            add_book(books)

        elif user_choice == "M":
            books = mark_books(books)

        else:
            print("undefined input")

        user_choice = input(MENU).upper().strip()

    save_book_file(books)

    print("so many books, so little time. Frank Zappa")

def list_all_books(books):
    """List all books in books."""
    number_of_required_books = 0
    index = 1
    required_pages = 0
    for lines in books:
        if lines[-1] == REQUIRED:
            symbol = '*'
            number_of_required_books += 1
            required_pages += lines[2]
        else:
            symbol = ' '

        print('{}{:2}.{:40} by {:17} {:3} pages'.format(symbol, index, lines[0], lines[1], str(lines[2]).rjust(3)))
        index += 1

    print(f'You need to read {required_pages} pages in {number_of_required_books} books.')

def is_blank(b):
    """check if input is blank"""
    space_num = 0
    for i in b:
        if i == " ":
            space_num += 1
        elif i == "":
            return False
    if len(b) == space_num:
        return False
    else:
        return True

def get_pages():
    """get pages and check if input is a number """
    try:
        book_page = int(input('Page:'))
        while book_page <= 0:
            print("must be > 0")
            book_page = input("Page:")
        else:
            return book_page
    except ValueError:
        print('invalid input; enter a valid number')
        return get_pages()

def add_book(books):
    """add a new book"""
    title = input("Title:")
    author = input("Author:")
    # get info of new book
    if is_blank(title) is False or is_blank(author) is False:
        print("can not be blank")
        add_book(books)
        # mistake check
    page = get_pages()
    books.append([title, author, page, REQUIRED])
    print("{} by {}, ({} pages) added to Reading Tracker".format(title, author, page))
    return books

def mark_books(books):
    """ mark a book as completed in books.csv."""
    list_all_books(books)
    required_books = [book for book in books if book[3] == REQUIRED]
    # get required books
    if len(required_books) == 0:
        print('No books left to read. Why not add a new book?')
        # print a notification if no book left
    else:
        print('Enter the number of a book to mark as completed')
        is_valid_input = False
        while not is_valid_input:
            try:
                number_of_book = int(input('>>> ').strip()) - 1
                if len(books) >= number_of_book > 0:
                    if books[number_of_book][3] == REQUIRED:
                        # check if input is valid, if valid, mark the book as completed
                        books[number_of_book].pop()
                        books[number_of_book].append(COMPLETED)
                        print(f'{books[number_of_book][0]} from {books[number_of_book][1]} completed')
                        is_valid_input = True
                    else:
                        print(f'The Purpose of {books[number_of_book][0]} is completed')
                        is_valid_input = True
                elif number_of_book < 0:
                    print('Number must be >= 0')
                else:
                    print('Invalid book number')
            except ValueError:
                print('Invalid input; enter a valid number')
    return books

def save_book_file(books):
    """Save books into books.csv"""
    book_file = open(FILE_DIRECTORY, "w")
    for book in books:
        book[-2] = str(book[-2])
        book_file.write(','.join(book) + "\n")
    book_file.close()
    print(f'{len(books)} books saved to books.csv')

if __name__ == '__main__':
    main()


