
from flask.globals import session
from models.songmodel import SongModel
from datetime import datetime
import sys
class Song:
    """
        The class has four parameters, the format of 
        uploadtime is "%Y-%m-%d,
        and length is always positive"
    """
    def __init__(self,id,name,length,uploadtime):
        self.id = id
        self.name = name
        self.length = length
        self.uploadtime = uploadtime

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
        if len(value)>100 or len(value)<1:
            raise Exception
        self._name = value

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
        song = SongModel.find_by_id(self.id)
        if song:
            return {"message":"Already song with such ID is there","code":404}
        songmodel = SongModel(self.id,self.name,self.length,self.uploadtime)
        songmodel.add_to_db()
        return {"message":"Added the song","code":200}

    @classmethod
    def delete(cls,id):
        song = SongModel.find_by_id(id)
        if not song:
            return {"message":"No song with such ID","code":404}
        song.delete_from_db()
        return {"message":"Item deleted","code":200}

    def update(self,id):
        song = SongModel.find_by_id(id)
        if not song:
            return {"message":"No song with such ID","code":404}
        song.name=self.name
        song.length = self.length
        song.uploadtime = self.uploadtime
        song.add_to_db()
        return {"message":"Item update","code":200}
    @classmethod
    def get(cls,id=None):
        if id is None:
            songs = SongModel.query.all()
            return {"message":[x.to_json() for x in songs],"code":200}
        song  = SongModel.find_by_id((id))
        if not song:
            return {"message":"No song with such ID","code":404}
        return {"message":[song.to_json()],"code":200}
        
        