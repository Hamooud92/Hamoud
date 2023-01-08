class Book():
    def __init__(self,title,author,pages):
        self.book_title=title
        self.book_uthor=author
        self.book_pages=pages
    #special method for strings
    def __str__(self):
        return f"{self.book_title} by {self.book_uthor} number of pages {self.book_pages}"
    def __len__(self):
        return self.book_pages
    def __del__(self):
        print("the object has been deleted")

b=Book('python rocks ','jose',200)
print(b)
print(str(b))
print(len(b))