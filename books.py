from sqlalchemy import Integer, Column, String, Date, ForeignKey

from base import Base


class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    genre = Column(String)
    page_count = Column(Integer)
    release_date = Column(Date)
    author_id = Column(Integer, ForeignKey('authors.id'))
