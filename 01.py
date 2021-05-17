import pickle
import dill
import datetime


class Book:
    ISBN: int
    name: str
    author: str
    publisher: str
    publish_date: datetime.date

    def __init__(self,ISBN , name , author,publish_date,publisher):
        self.ISBN = ISBN
        self.name = name
        self.author = author
        self.publisher = publisher
        self.publish_date = publish_date


with open("books.pkl") as f:
    un = pickle.loads(f.read())
    print(un)