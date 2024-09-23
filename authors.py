from sqlalchemy import Column, Integer, String, Date
from base import Base


class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    birth_date = Column(Date)
    birth_place = Column(String)



