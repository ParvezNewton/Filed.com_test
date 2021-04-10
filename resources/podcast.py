
from datetime import datetime
from models.podcastmodel import PodcastModel
class Podcast:
    def __init__(self,id,name,length,uploadtime,host,participants=[]):
        self.id = id
        self.name = name
        self.length = length
        self.uploadtime = uploadtime
        self.host = host
        self.participants = participants

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

    @property
    def host(self):
        return self._host

    @host.setter
    def host(self,value):
        if len(value)>100 or len(value)<1:
            raise Exception
        self._host = value
    
    @property
    def participants(self):
        return self._participants

    @participants.setter
    def participants(self,value):
        self._participants = ",".join(value)

    def create(self):
        podcast = PodcastModel.find_by_id(self.id)
        if podcast:
            return {"message":"Already podcast with such ID is there","code":404}
        podcastmodel = PodcastModel(self.id,self.name,self.length,self.uploadtime,self.host,self.participants)
        podcastmodel.add_to_db()
        return {"message":"Added the podcast","code":200}

    @classmethod
    def delete(cls,id):
        podcast = PodcastModel.find_by_id(id)
        if not podcast:
            return {"message":"No podcast with such ID","code":404}
        podcast.delete_from_db()
        return {"message":"Item deleted","code":200}

    def update(self,id):
        podcast = PodcastModel.find_by_id(id)
        if not podcast:
            return {"message":"No podcast with such ID","code":404}
        podcast.name=self.name
        podcast.length = self.length
        podcast.uploadtime = self.uploadtime
        podcast.host = self.host
        podcast.participants = self.participants
        podcast.add_to_db()
        return {"message":"Item update","code":200}

    @classmethod
    def get(cls,id=None):
        if id is None:
            podcasts = PodcastModel.query.all()
            return {"message":[x.to_json() for x in podcasts],"code":200}
        podcast  = PodcastModel.find_by_id((id))
        if not podcast:
            return {"message":"No podcast with such ID","code":404}
        return {"message":[podcast.to_json()],"code":200}
        