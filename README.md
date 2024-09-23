project generates author and book tables using sqlalchemy orm.

data is mostly randomized by Faker and random modules


sqlite should be already installed along python

requirements
```
python3 -m pip install sqlalchemy
python3 -m pip install Faker
```


(optional if sqlite is not available)

on Debian based:
```
sudo apt update
sudo apt install sqlite3 libsqlite3-dev
```
on macOS:
```
brew install sqlite
```

You are welcome for suggestions about querying authors without books
I believe there is better way than: 

> authors_without_books = session.query(Author).outerjoin(Book).filter(Book.id == None).all()

I was trying to come up with solution in alchemy orm analogue to:
> SELECT * FROM authors a WHERE (SELECT COUNT(*) FROM books b WHERE b.author_id = a.id) = 0

but querying with join also works

