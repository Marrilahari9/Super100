class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

class Member:
    def __init__(self, name, membership_id):
        self.name = name
        self.membership_id = membership_id
        self.books_borrowed = []

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def borrow_book(self, book_isbn, member_id):
        book = self.find_book(book_isbn)
        member = self.find_member(member_id)

        if book and book.available and member:
            book.available = False
            member.books_borrowed.append(book)
            print(f"{member.name} borrowed {book.title} successfully.")
        else:
            print("Book not available or member not found.")

    def return_book(self, book_isbn, member_id):
        book = self.find_book(book_isbn)
        member = self.find_member(member_id)

        if book and not book.available and member and book in member.books_borrowed:
            book.available = True
            member.books_borrowed.remove(book)
            print(f"{member.name} returned {book.title} successfully.")
        else:
            print("Book not borrowed by this member or not found.")

    def find_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def find_member(self, member_id):
        for member in self.members:
            if member.membership_id == member_id:
                return member
        return None

    def track_available_books(self):
        available_books = [book for book in self.books if book.available]
        print("Available books:")
        for book in available_books:
            print(f"- {book.title} by {book.author}")

# Example usage
library = Library()
b1 = Book("King Lear", "Willian Shakespear", "21A31A4288")
b2 = Book("Profit First", "Benjamin Graham", "98488668597")
library.add_book(b1)
library.add_book(b2)

m1 = Member("Lahari", "1234")
library.add_member(m1)

library.borrow_book("21A31A4288", "1234")  # Borrow book1
library.track_available_books()          # Only book2 is available
