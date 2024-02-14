class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self.__name = name
        self.__author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f'Book({self.__class__.__name__}(name={self.name!r}, author={self.author!r})'


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        self.pages = pages
        super().__init__(name, author)

    @classmethod
    def check(cls, pages):
        if type(pages) != int:
            raise TypeError("Недопустимый тип значений")

    def __repr__(self) -> str:
        return f'PaperBook ({self.name!r},{self.author!r},{self.pages!r})'


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        self.duration = duration
        super().__init__(name, author)


    @classmethod
    def check(cls, duration):
        if type(duration) != float:
            raise TypeError("Недопустимый тип значений")

    def __repr__(self) -> str:
        return f' AudioBook ({self.name!r},{self.author!r},{self.pages!r},{self.duration!r})'

