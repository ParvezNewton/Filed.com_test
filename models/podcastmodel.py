from db import db

class PodcastModel(db.Model):
    __tablename__ = "podcast"


    id = db.Column(db.Integer,unique=True,primary_key=True)
    name = db.Column(db.String(100),nullable=False)
    length= db.Column(db.Integer)
    uploadtime = db.Column(db.DateTime)
    host = db.Column(db.String(100),nullable=False)
    participants = db.Column(db.Text)

    def __init__(self,id,name,length,uploadtime,host,participants):
        self.id = id
        self.name = name
        self.length = length
        self.uploadtime = uploadtime
        self.host = host
        self.participants = participants

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
        return {"id":self.id ,"name":self.name,"length":self.length,"uploadtime":self.uploadtime,
                "host":self.host,"participants":self.participants.split(",")} 

