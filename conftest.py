import pytest
from main import BooksCollector

@pytest.fixture
def collector():
    collector = BooksCollector()
    return collector

@pytest.fixture
def collection_genre(collector):
    collector.add_new_book('Чудеса в решете')
    collector.set_book_genre('Чудеса в решете', 'Комедии')
    collector.add_new_book('Гостья из будущего')
    collector.set_book_genre('Гостья из будущего', 'Фантастика')
    collector.add_new_book('Паранормальные явления')
    collector.set_book_genre('Паранормальные явления', 'Ужасы')
    return collector.books_genre
