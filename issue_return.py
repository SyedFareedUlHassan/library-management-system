def issue_book(library, isbn, member):
    if isbn in library.books and library.books[isbn].copies > 0:
        library.books[isbn].copies -= 1
        member.borrowed_books.append(isbn)