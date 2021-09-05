class Book:
    author = ""
    title = ""
    def __init__(self, author, title):
        self.author = author
        self.title = title
    def display(self):
        print(self.title+" written by "+self.author)


if __name__ == "__main__":
    book1 = Book("John Steinbeck","Of Mice and Men")
    book2 = Book("Harper Lee","To Kill a Mockingbird")
    book1.display()
    book2.display()
