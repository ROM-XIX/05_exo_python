class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year


class Library:
    def __init__(self):
        self.books = []
        self.borrow_books = []

    # Ajouter les méthodes ici
    def add_book(self, book):
        """Ajoute un livre à la bibliothèque."""
        self.books.append(book)
        a = print(f"Le livre '{book.title}' a été ajouté à la bibliothèque.")
        return a

    def remove_book(self, book_title):
        """Supprime un livre de la bibliothèque en utilisant le titre du livre comme argument."""
        for book in list(self.books):
            if book.title == book_title:
                self.books.remove(book)
                a = print(f"Le livre '{book_title}' a été supprimé de la bibliothèque.")
                return a
        print(f"Le livre '{book_title}' n'a pas été trouvé.")

    def borrow_book(self, book_title):
        """Emprunte un livre de la bibliothèque en utilisant le titre du livre comme argument.
        arg : book_title
        Le livre doit être retiré de la liste des livres disponibles et
        ajouté dans la liste des livres empruntés.
        """
        for book in list(self.books):
            if book.title == book_title:
                self.borrow_books.append(book)
                self.books.remove(book)
                a = print(f"Le livre '{book_title}' est maintenant en prêt.")
                return a
        print(f"Le livre '{book_title}' n'ai pas disponible.")

    def return_book(self, book_title):
        """Rend un livre emprunté à la bibliothèque en utilisant le titre du livre comme argument.
        Le livre doit être retiré de la liste des livres empruntés et ajouté dans la liste des livres disponibles.
        """
        for borrow_book in list(self.borrow_books):
            if borrow_book.title == book_title:
                self.books.append(borrow_book)
                self.borrow_books.remove(borrow_book)
                a = print(f"Le livre '{book_title}' est retourné à la bibli")
                return a
        print(f"Le livre '{book_title}' n'a pas était trouvé.")

    def available_books(self):
        """Renvoie une liste contenant les titres des livres disponibles dans la bibliothèque."""
        books_available = []
        for book in self.books:
            books_available.append(book.title)
        a = print(books_available)
        return a

    def borrowed_books(self):
        """Renvoie une liste contenant les titres des livres empruntés de la bibliothèque."""
        list_borrow_books = []
        for book in self.borrow_books:
            list_borrow_books.append(book.title)
        a = print(list_borrow_books)
        return a

# ==== Démonstration de la classe Library ====

# Création de quelques livres
book1 = Book("1984", "George Orwell", 1949)
book2 = Book("Le Petit Prince", "Antoine de Saint-Exupéry", 1943)
book3 = Book("Dune", "Frank Herbert", 1965)

# Création de la bibliothèque
lib = Library()

# Ajout de livres
lib.add_book(book1)
lib.add_book(book2)
lib.add_book(book3)
print()
print()


# Afficher les livres disponibles
lib.available_books()

# Emprunter un livre
lib.borrow_book("Dune")
lib.available_books()
lib.borrowed_books()
print()
# Essayer d'emprunter le même livre à nouveau
print("ici")
lib.borrow_book("Dune")
print()
print("ici")

# Rendre le livre
lib.return_book("Dune")
lib.available_books()
lib.borrowed_books()
print()

# Supprimer un livre de la bibliothèque
lib.remove_book("1984")
lib.available_books()
