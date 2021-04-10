from db import db

class AudioBookModel(db.Model):
    __tablename__ = "audiobook"


    id = db.Column(db.Integer,unique=True,primary_key=True)
    narrator = db.Column(db.String(100),nullable=False)
    title = db.Column(db.String(100),nullable=False)
    author = db.Column(db.String(100),nullable=False)
    length= db.Column(db.Integer)
    uploadtime = db.Column(db.DateTime)

    def __init__(self,id,length,uploadtime,narrator,title,author):
        self.id = id
        self.length = length
        self.uploadtime = uploadtime 
        self.narrator = narrator
        self.title = title
        self.author = author

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
        return {"id":self.id ,"narrator":self.narrator,"length":self.length,"uploadtime":self.uploadtime,
                "title":self.title,"author":self.author}   
