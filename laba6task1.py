class Library():
    all_books = []
    name = "Morning magic"
    author = "Arrmon Abedikichi"
    def __init__(self, name, author):
        self.name = name
        self.author = author

    def add_book_in_lib(self):
        book = dict([("Author", self.author), ("Name", self.name)])
        self.all_books.append(book)
    def find_book(self. author = "Arrmon Abedikichi", name = "Morning magic"):
        for i in self.all_books:
            if i["Author"] == author or i["Name"] == name:
                print(i)

    def remove_book_from_lib(self, author = "Arrmon Abedikichi", name = "Morning magic"):
        count = 0
        for i in self.all_books:
            count +=1
            if i ["Author"] == author or i["Name"] == name:
                print(self.all_books)


book = Library()
book_2 = Library()
book_2.add_book_in_lib()
book_add_book_in_lib()
book.print_all_books()
book.find_book()

lib = Library("Morning magic", "Zahar Berkut")
lib.print_all_books()








            
