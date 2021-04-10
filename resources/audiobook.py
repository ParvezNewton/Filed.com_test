
from datetime import datetime
from models.audiobookmodel import AudioBookModel


class AudioBook:
    def __init__(self,id,length,uploadtime,narrator,title,author):
        self.id = id
        self.length = length
        self.uploadtime = uploadtime 
        self.narrator = narrator
        self.title = title
        self.author = author

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self,value):
        if len(value)>100 or len(value)<1:
            raise Exception
        self._author = value

    @property
    def narrator(self):
        return self._narrator

    @narrator.setter
    def narrator(self,value):
        if len(value)>100 or len(value)<1:
            raise Exception
        self._narrator = value

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self,value):
        if len(value)>100 or len(value)<1:
            raise Exception
        self._title = value

    @property
    def length(self):
        return self._length
    
    @length.setter
    def length(self,value):
        if value < 0:
            raise ValueError
        self._length = value
    @property
    def uploadtime(self):
        return self._uploadtime

    @uploadtime.setter
    def uploadtime(self,date):
        try:
            
            today_date = datetime.today()
            date_check = datetime.strptime(date,"%Y-%m-%d")
            val = (today_date-date_check)
            if val.days <= 0:
                    self._uploadtime = date_check
            else:
                    raise Exception
        except:
            raise ValueError("format not correct")


    def create(self):
        audiobook = AudioBookModel.find_by_id(self.id)
        if audiobook:
            return {"message":"Already audiobook with such ID is there","code":404}
        audiobook = AudioBookModel(self.id,self.length,self.uploadtime,self.narrator,self.title,self.author)
        audiobook.add_to_db()
        return {"message":"Added the audiobook","code":200}

    @classmethod
    def delete(cls,id):
        audiobook = AudioBookModel.find_by_id(id)
        if not audiobook:
            return {"message":"No audiobook with such ID","code":404}
        audiobook.delete_from_db()
        return {"message":"Item deleted","code":200}

    def update(self,id):
        audiobook = AudioBookModel.find_by_id(id)
        if not audiobook:
            return {"message":"No audiobook with such ID","code":404}
        audiobook.narrator=self.narrator
        audiobook.length = self.length
        audiobook.uploadtime = self.uploadtime
        audiobook.author = self.author
        audiobook.title = self.title
        audiobook.add_to_db()
        return {"message":"Item update","code":200}

    @classmethod
    def get(cls,id=None):
        if id is None:
            audiobooks = AudioBookModel.query.all()
            return {"message":[x.to_json() for x in audiobooks],"code":200}
        audiobook  = AudioBookModel.find_by_id((id))
        if not audiobook:
            return {"message":"No audiobook with such ID","code":404}
        return {"message":[audiobook.to_json()],"code":200}