from sqlalchemy import Column, Integer, String
from database import Database

db = Database()

class Webpage(db.base):
    __tablename__ = 'webpages'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    url = Column(String)
    description = Column(String)

    def __repr__(self):
        return "<Webpage(title='%s', url='%s', description='%s')>" % (self.title, self.url, self.description)
