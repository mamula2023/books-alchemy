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
