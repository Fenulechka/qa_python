import pytest

class TestBooksCollector:
    def test_books_genre_init(self, collector):
        assert collector.books_genre == {}

    def test_favorites_init(self, collector):
        assert collector.favorites == []

    def test_genre_init(self, collector):
        assert collector.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']

    def test_genre_age_rating_init(self, collector):
        assert collector.genre_age_rating == ['Ужасы', 'Детективы']


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
        assert collector.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
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

    def test_get_books_with_specific_genre(self, collector, collection_genre, genre, expected):
        result = collector.get_books_with_specific_genre(genre)
        assert result == expected


    @pytest.mark.parametrize("expected_genres",
                            [({'Чудеса в решете': 'Комедии', 'Гостья из будущего': 'Фантастика', 'Паранормальные явления': 'Ужасы'})])

    def test_get_books_genre(self, collector, collection_genre, expected_genres):
        result = collector.get_books_genre()
        assert result == expected_genres


    @pytest.mark.parametrize("expected_books",
                            [(['Чудеса в решете', 'Гостья из будущего'])])

    def test_get_books_for_children(self, collector, collection_genre, expected_books):
        result = collector.get_books_for_children()
        assert result == expected_books


    @pytest.mark.parametrize("book_name, expected_favorites",
                            [('Чудеса в решете', ['Чудеса в решете']), ('Какая-то книга', [])])

    def test_add_book_in_favorites(self, collector, collection_genre, book_name, expected_favorites):
        collector.favorites.clear()
        collector.add_book_in_favorites(book_name)
        assert collector.favorites == expected_favorites


    @pytest.mark.parametrize("book_name, expected_favorites",
                            [('Чудеса в решете', ['Гостья из будущего', 'Паранормальные явления']),
                            ('Гостья из будущего', ['Чудеса в решете', 'Паранормальные явления']),
                            ('Какая-то книга', ['Чудеса в решете', 'Гостья из будущего', 'Паранормальные явления']),
                            ('Паранормальные явления', ['Чудеса в решете', 'Гостья из будущего'])
                            ])

    def test_delete_book_from_favorites(self, collector, collection_genre, book_name, expected_favorites):
        collector.add_book_in_favorites('Чудеса в решете')
        collector.add_book_in_favorites('Гостья из будущего')
        collector.add_book_in_favorites('Паранормальные явления')
        collector.delete_book_from_favorites(book_name)
        assert collector.favorites == expected_favorites


    @pytest.mark.parametrize("expected_favorites",
                             [(['Гостья из будущего', 'Паранормальные явления'])])

    def test_get_list_of_favorites_books(self, collector, collection_genre, expected_favorites):
        collector.favorites.clear()
        collector.add_book_in_favorites('Гостья из будущего')
        collector.add_book_in_favorites('Паранормальные явления')
        result = collector.get_list_of_favorites_books()
        assert result == expected_favorites
