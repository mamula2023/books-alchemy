import random
from datetime import datetime, timedelta
from platform import release

from faker import Faker
from sqlalchemy import func

from authors import Author
from books import Book


class Generator:
    def __init__(self, session):
        self.session = session
        self.fake = Faker()

    def generate_authors(self, count):
        for i in range(count):
            first_name = self.fake.first_name()
            last_name = self.fake.last_name()
            birth_date = self.fake.date_between(start_date='-1000y', end_date='-18y')
            birth_place = self.fake.city()
            author = Author(first_name=first_name, last_name=last_name, birth_date=birth_date, birth_place=birth_place)
            self.session.add(author)
        self.session.commit()

    def generate_books(self, count):
        genres = ['Romance', 'Mystery', 'Science Fiction', 'Thriller', 'Biography', 'Inspirational', 'Fantasy',
                  'Horror']
        for i in range(1000):
            title = self.fake.sentence(5, True)
            genre = random.choice(genres)
            page_count = random.randint(1, 2000)

            random_author = self.session.query(Author).order_by(func.random()).first()

            date_str = str(random_author.birth_date)

            release_date = random_release_date(date_str)

            book = Book(title=title, genre=genre, page_count=page_count,
                        release_date=release_date, author_id=random_author.id)
            self.session.add(book)

        self.session.commit()


def random_release_date(author_birth_date):

    birth_date = datetime.strptime(author_birth_date, '%Y-%m-%d')

    if birth_date.month == 2 and birth_date.day == 29:
        birth_date = birth_date.replace(day=28)
    release_start = birth_date.replace(year=birth_date.year + 18)
    max_year = min(birth_date.year + 100, datetime.today().year)
    release_end = birth_date.replace(year=max_year)
    offset_range = (release_end - release_start).days
    random_day_offset = random.randint(0, offset_range)

    release_date = release_start + timedelta(random_day_offset)

    return release_date.date()

