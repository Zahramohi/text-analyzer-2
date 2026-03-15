# ---------- Person Class Example ----------

class Person:

    def init(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print("Hello, my name is", self.name)
        print("I am", self.age, "years old")


p1 = Person("Zahra", 30)
p1.introduce()


# ---------- Book Class Exercise ----------

class Book:

    def init(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def info(self):
        print(f"This book is {self.title} by {self.author}")


my_book = Book("Python Basics", "Zahra", 200)
my_book.info()


# ---------- Algorithm Exercise 1 ----------
numbers = [3,7,2,9,5]
print("Largest number:", max(numbers))


# ---------- Algorithm Exercise 2 ----------
numbers = [1,2,3,4,5,6]

for n in numbers:
    if n % 2 == 0:
        print(n)