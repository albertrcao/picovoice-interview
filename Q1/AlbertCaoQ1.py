# Albert Cao
# 07/24/21

### Question 1

# Assume we have a function get_book_info(isbn) that takes a string ISBN argument and retrieves a
# struct/object containing the Title, Author, and Language of a book (each represented as a string) from a
# database. Write a wrapper function that increases performance by keeping some of the database results in
# memory for quick lookup.

# To prevent memory from growing unbounded, we only want to store a maximum of N book records. At any
# given time, we should be storing the N books that we accessed most recently. Assume that N can be a large
# number when making decisions about choices of data structure(s) and algorithm(s).

from typing import NamedTuple

# Declaring a class for a book object.
class Book(NamedTuple):
    title: str
    author: str
    lang: str

# A dict (queue) to store the n most recent results.
recent_results = {}
# Setting n to 3 for testing purposes. Change to modify the maximum number of recent records!
n = 3

# Creating some books for testing purposes.
fellowship = Book("The Fellowship of the Ring", "J. R. R. Tolkien", "English")
f_isbn =  9780007136599

towers = Book("The Two Towers", "J. R. R. Tolkien", "English")
t_isbn = 9780007203598

king = Book("The Return of the King", "J. R. R. Tolkien", "English")
k_isbn = 9780007203604

hobbit = Book("The Hobbit", "J. R. R. Tolkien", "English")
h_isbn = 9780048232731

# A dummy function simulating the real get_book_info() function.
def get_book_info(isbn):
    # Searches database for ISBN number...
    # Finds book object and returns it...
    if (isbn == f_isbn):
        return fellowship
    elif (isbn == t_isbn):
        return towers
    elif (isbn == k_isbn):
        return king
    elif (isbn == h_isbn):
        return hobbit

# A wrapper function that keeps some of the database results in memory for quick lookup.
def get_book_faster(isbn, n):
    # Pointing the function to the recent results queue.
    global recent_results

    # If the ISBN has been recently searched, return it.
    if (isbn in recent_results):
        print("BOOK FOUND IN RECENTS")
        return recent_results[isbn]
    # Otherwise, add it to recent results.
    else:
        # First, find the book using the original function.
        this_book = get_book_info(isbn)

        # If the recent_results dict is not full, then add the new book.
        if (len(recent_results) != n):
            print("BOOK ADDED TO RECENTS")
            recent_results[isbn] = this_book
        # If the recent_results dict is full, then pop the first book and add the new one.
        else:
            recent_results.pop(list(recent_results.keys())[0])
            print("BOOK ADDED TO RECENTS")
            recent_results[isbn] = this_book

    return this_book

if (__name__ == "__main__"):
    print("---------------------------------------------")
    print("Albert Cao - Picovoice Interview - Question 1")
    print("---------------------------------------------")
    # recent_results is empty, fellowship will be added.
    get_book_faster(f_isbn, n)
    # fellowship exists in recent_results, fellowship will be found.
    get_book_faster(f_isbn, n)
    # fellowship is in recent_results, towers will be added.
    get_book_faster(t_isbn, n)
    # fellowship and towers are in recent_results, king will be added.
    get_book_faster(k_isbn, n)
    # king exists in recent_results, king will be found.
    get_book_faster(k_isbn, n)
    # recent_results is full, fellowship will be popped and hobbit will be added.
    get_book_faster(h_isbn, n)
    # recent_results is full, towers will be popped and fellowship will be added.
    get_book_faster(f_isbn, n)
    print("---------------------------------------------")
    # Books in recent_results should be: king, hobbit, fellowship.
    print(recent_results)
    print("---------------------------------------------")