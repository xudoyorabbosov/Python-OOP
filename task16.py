class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_read = False

    def mark_as_read(self):
        self.is_read = True

    def status(self):
        holat = "O'qilgan" if self.is_read else "O'qilmagan"
        print(f"{self.title}: {holat}")

books = [
    Book("Alkimyogar", "Paulo Koelo"),
    Book("Ufq", "Pirimqul Qodirov"),
    Book("Shum bola", "G'afur G'ulom"),
    Book("Dunyo ishlari", "O'tkir Hoshimov"),
    Book("Ikki eshik orasi", "Erkin A'zam")
]

books[1].mark_as_read()
books[3].mark_as_read()

for book in books:
    book.status()

print("\nO'qilgan kitoblar:")
for book in books:
    if book.is_read:
        print(book.title)
