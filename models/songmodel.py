from enum import unique
from operator import le
from db import db

class SongModel(db.Model):
    __tablename__ = "songs"

    id = db.Column(db.Integer,unique=True,primary_key=True)
    name = db.Column(db.String(100),unique=True,nullable=False)
    length= db.Column(db.Integer)
    uploadtime = db.Column(db.DateTime)

    def __init__(self,id,name,length,uploadtime):
        self.id = id
        self.name = name
        self.length = length
        self.uploadtime = uploadtime

    def add_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls,id):
        return cls.query.filter_by(id=id).first()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def to_json(self):
        return {"id":self.id ,"name":self.name,"length":self.length,"uploadtime":self.uploadtime}   

