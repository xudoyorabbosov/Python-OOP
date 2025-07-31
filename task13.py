class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_read = False

    def mark_as_read(self):
        self.is_read = True

    def status(self):
        if self.is_read:
            print(f"{self.title}: O'qilgan")
        else:
            print(f"{self.title}: O'qilmagan")

books = [
    Book("Sariq devning minib kelishi", "Xudoyberdi To'xtaboyev"),
    Book("Ufq", "Pirimqul Qodirov"),
    Book("Alkimyogar", "Paulo Koelo"),
    Book("Shum bola", "G'afur G'ulom")
]

books[0].mark_as_read()
books[2].mark_as_read()

for book in books:
    book.status()
