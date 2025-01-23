from datetime import date

# Завдання 1
#
# Створіть клас, який описує книгу. Він повинен містити інформацію про автора, 
# назву, рік видання та жанр. Створіть кілька різних книжок. 
# Визначте для нього методи _repr_ та _str_.
#
#
# Завдання 2
#
# Створіть клас, який описує відгук до книги. 
# Додайте до класу книги поле – список відгуків. 
# Зробіть так, щоб при виведенні книги на екран за допомогою функції print також виводилися відгуки до неї. 


class Book:
    def __init__(
            self, 
            author: str, 
            name: str, 
            published_at: date, 
            publisher: str, 
            genres: list[str],
            reviews: list[str] | None = None,
        ):
        self.author = author
        self.name = name
        self.published_at = published_at
        self.publisher = publisher
        self.genres = genres
        self.reviews = reviews
    
    def print_info(self):
        print(f"<{self.author} - {self.name}> {self.published_at}")
        print("Genres:", ", ".join(self.genres))
        print(f"Publisher: {self.publisher}")
        if self.reviews:
            print("Reviews\n", "\n\n".join(self.reviews))
        else:
            print("No reviews provided")

    def __str__(self) -> str:
        return f"<{self.author} - {self.name}> {", ".join(self.genres)}, ({self.publisher}, {self.published_at})"
    
    def __repr__(self) -> str:
        return f"<Book({self.author}, {self.name}, {self.genres}, {self.publisher}, {self.published_at}) {id(self)}>"


the_witcher = Book(
    author="Andrzej Sapkowski",
    name="The Witcher: Blood of Elves",
    published_at=date(1994, 8, 25),
    publisher="superNOWA",
    genres=["medieval", "fantasy", "fight"],
    reviews=[
        "Nice book! I'm really into such adventures and easy to read.",
        "I'm a big fan, especially of this author.",
        "Is it really was published at 1994?",
    ]
)

harry_potter = Book(
    author="J.K. Rowling",
    name="Harry Potter: Philosopher's stone",
    published_at=date(1997, 3, 25),
    publisher="Bloomsbury",
    genres=["magic", "fantasy", "adventures"]
)

print(str(the_witcher))
print(str(harry_potter))
print()
print(repr(the_witcher))
print(repr(harry_potter))
print()
the_witcher.print_info()
harry_potter.print_info()
