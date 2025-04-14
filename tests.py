import pytest

class TestBooksCollector:

    @pytest.mark.parametrize("book_name, expected",
                            [("Унесенные ветром", True), ("", False), ("A" * 42, False), ("Гордость и предубеждение", True)])

    def test_add_new_book(self, collector, book_name, expected):
        collector.add_new_book(book_name)
        if expected:
            assert book_name in collector.books_genre
        else:
            assert book_name not in collector.books_genre

    def test_set_book_genre_valid(self, collector):
        collector.books_genre['Полианна'] = ''
        collector.set_book_genre('Полианна', 'Мультфильмы')
        assert collector.books_genre['Полианна'] == 'Мультфильмы'

    def test_get_book_genre_valid(self, collector):
        collector.books_genre = {'Чудеса в решете': 'Комедии', 'Гостья из бужущего': 'Фантастика'}
        assert collector.get_book_genre('Гостья из бужущего') == 'Фантастика'

    def test_get_book_genre_not_valid(self, collector):
        assert collector.get_book_genre('Какая-то книга') is None

    @pytest.mark.parametrize("genre, expected",
                            [('Ужасы', ['Паранормальные явления']),
                            ('Фантастика', ['Гостья из будущего']),
                            ('Романтика', []),
                            ('Детективы', [])
                            ])

    def test_get_books_with_specific_genre(self, collector, genre, expected):
        collector.add_new_book('Гостья из будущего')
        collector.set_book_genre('Гостья из будущего', 'Фантастика')
        collector.add_new_book('Паранормальные явления')
        collector.set_book_genre('Паранормальные явления', 'Ужасы')
        result = collector.get_books_with_specific_genre(genre)
        assert result == expected

    def test_get_books_genre(self, collector):
        collector.add_new_book('Чудеса в решете')
        collector.set_book_genre('Чудеса в решете', 'Комедии')
        collector.add_new_book('Гостья из будущего')
        collector.set_book_genre('Гостья из будущего', 'Фантастика')
        collector.add_new_book('Паранормальные явления')
        collector.set_book_genre('Паранормальные явления', 'Ужасы')
        expected_genres = {'Чудеса в решете': 'Комедии', 'Гостья из будущего': 'Фантастика', 'Паранормальные явления': 'Ужасы'}
        result = collector.get_books_genre()
        assert result == expected_genres

    def test_get_books_for_children(self, collector):
        collector.add_new_book('Лунтик')
        collector.set_book_genre('Лунтик', 'Мультфильмы')
        collector.add_new_book('Простоквашино')
        collector.set_book_genre('Простоквашино', 'Мультфильмы')
        expected_books = ['Лунтик', 'Простоквашино']
        result = collector.get_books_for_children()
        assert result == expected_books

    def test_add_known_book_in_favorites(self, collector):
        collector.add_new_book('Чудеса в решете')
        collector.add_book_in_favorites('Чудеса в решете')
        assert len(collector.favorites) == 1
        assert 'Чудеса в решете' in collector.favorites

    def test_add_unknown_book_in_favorites(self, collector):
        collector.add_book_in_favorites('Незнакомая книга')
        assert len(collector.favorites) == 0
        assert 'Незнакомая книга' not in collector.favorites

    def test_delete_existing_book_from_favorites(self, collector):
        collector.add_new_book('Паранормальные явления')
        collector.add_book_in_favorites('Паранормальные явления')
        collector.delete_book_from_favorites('Паранормальные явления')
        assert collector.favorites == []

    def test_get_list_of_favorites_books(self, collector):
        assert collector.get_list_of_favorites_books() == []
        collector.add_new_book('Гостья из будущего')
        collector.add_book_in_favorites('Гостья из будущего')
        collector.add_new_book('Паранормальные явления')
        collector.add_book_in_favorites('Паранормальные явления')
        expected_favorites = ['Гостья из будущего', 'Паранормальные явления']
        result = collector.get_list_of_favorites_books()
        assert result == expected_favorites
