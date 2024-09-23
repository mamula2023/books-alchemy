from sqlalchemy import create_engine, func, desc, select
from sqlalchemy.orm import sessionmaker
from authors import Author
from base import Base
from books import Book


from generator import Generator

if __name__ == '__main__':
    engine = create_engine('sqlite:///test.db')

    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    generator = Generator(session)

    generator.generate_authors(500)
    generator.generate_books(1000)
    session.commit()

    max_number_pages = session.query(func.max(Book.page_count)).scalar()

    most_pages_book = session.query(Book).filter(Book.page_count == max_number_pages).all()

    print("books with most pages: ")

    for i in range(len(most_pages_book)):
        book = most_pages_book[i]
        author = session.query(Author).filter(Author.id == book.author_id).scalar()

        print(str(i + 1) + ". \"" + book.title + "\" by", author.first_name, author.last_name, "released in",
              book.release_date)
        print("\t", "genre:", book.genre)
        print("\t", "page count:", book.page_count)

    avg_count = session.query(func.avg(Book.page_count)).scalar()

    print("average count of pages is", avg_count)

    youngest_author = session.query(Author).order_by(desc(Author.birth_date)).first()

    print("youngest author is", youngest_author.first_name, youngest_author.last_name, "(born",
          (str(youngest_author.birth_date) + ")"))

    print("Authors without books: ")
    authors_without_books = session.query(Author).outerjoin(Book).filter(Book.id == None).all()

    for i in range(len(authors_without_books)):
        print(str(i + 1), authors_without_books[i].first_name, authors_without_books[i].last_name)


