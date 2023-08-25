#data buku yang tersedia
books = [
    {"id":"801","title": "Dune Messiah", "author": "Frank Herbert", "borrowed": False},
    {"id":"802","title": "Metamorphosis", "author": "Franz Kafka", "borrowed": False},
    {"id":"803","title": "War And Peace", "author": "Leo Tolstoy", "borrowed": False},
    {"id":"804","title": "The Last Wish", "author": "Andrzej Sapkowski", "borrowed": False}
]

def view_books(): #fungsi untuk menampilkan buku yang ada di perpustakaan
    print('||\t ID \t|\t TITLE \t\t|\t AUTHOR \t|\t STATUS \t||')
    for book in books:
        status = "available" if not book["borrowed"] else "lent out"
        print(f"||\t{book['id']}\t|{book['title']}\t \t| {book['author']} \t| {status} \t\t||")

def remove_book(title): #fungsi untuk menghapus data buku
    for book in books:
        if book["title"].lower() == title:
            books.remove(book)
            print(f"\nBook '{title.title()}' removed from the library.\n")
            view_books()
            return
    else: 
        print(f"\nBook '{title.title()}' not found in the library.\n")
        view_books()

def lend_book(title,user): #fungsi untuk meminjamkan buku
    for book in books:
        if book["title"].lower() == title:
            if not book["borrowed"]:
                book["borrowed"] = True
                print(f"\nBook '{title.title()}' lent out to {user.title()}.\n")
                borrowed_books()
                return
            else:
                print(f"\nBook '{title}' is already lent out.\n")
                view_books()
                return
    else:
        print(f"Book '{title.title()}' not found in the library.")
        view_books()

def borrowed_books(): #fungsi untuk menampilkan buku yang telah dipinjamkan saja
    for book in books:
        if book["borrowed"]:
            status = "available" if not book["borrowed"] else "lent out"
            print(f"||\t{book['id']}\t|{book['title']}\t \t| {book['author']} \t| {status} \t\t||")

def return_book(title,user): #fungsi untuk mengembalikan buku yang sudah dipinjam orang
    for book in books:
        if book["title"].lower() == title:
            if book["borrowed"]:
                book["borrowed"] = False
                print(f"\nBook '{title.title()}' returned by {user.title()}.\n")
                borrowed_books()
                return
            else:
                print(f"Book '{title.title()}' was not lent out.")
                view_books()
                return
    else:
        print(f"Book '{title.title()}' not found in the library.")
        view_books()

def add_book(id, title, author): #fungsi untuk menambahkan buku baru
    book = {"id":id, "title": title.title(), "author": author.title(), "borrowed": False}
    books.append(book)
    print(f"\nBook {id} '{title.title()}' by {author.title()} added to the library.\n")
    view_books()

#tampilan main menu
while True: 
    print('''\n===Welcome to The House of Wisdom Library===
    1. View all books
    2. Remove a book
    3. Lend a book
    4. Return a book
    5. Add a book 
    6. Exit''')
    choice = input("Enter your choice: ")
    if choice == "1":
        view_books()
    elif choice == "2":
        title = input("Enter the title of the book: ")
        remove_book(title)
    elif choice == "3":
        title = input("Enter the title of the book: ")
        user = input("Enter User Name: ")
        lend_book(title,user)
    elif choice == "4":
        title = input("Enter the title of the book: ")
        user = input("Enter User Name: ")
        return_book(title,user)
    elif choice == "5":
        try:
            id = int(input("Enter the ID of the book you want to add: "))
        except ValueError:
            print("\nInvalid input. Please enter a valid integer ID.")
            continue
        title = input("Enter the title of the book: ")
        author = input("Enter the author of the book: ")
        add_book(id,title, author)
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please try again.")

