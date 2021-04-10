from resources.audiobook import AudioBook
from resources.podcast import Podcast
from flask import Flask,request,jsonify
from resources.song import Song
from db import db
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///audio.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.before_first_request
def creatall():
    db.create_all()

@app.route("/create")
def create():
    param = request.get_json(force=True)
    if(param["aduioFileType"]=="song"):
        try:
            songDetails = param["audioFileMetadata"]
            newSong = Song(songDetails["ID"],songDetails["Name of the song"],songDetails["Duration in number of seconds"]
                           ,songDetails["Uploaded time"])
            response = newSong.create()
            return jsonify({"response":response["message"]}),response["code"]
        except:
            return jsonify({"response":"Bad Request"}),400    
    elif(param["aduioFileType"]=="podcast"):
        try:
            podcastDetails = param["audioFileMetadata"]
            if podcastDetails["Participants"]:
                newPodcast = Podcast(podcastDetails["ID"],podcastDetails["Name of the podcast"],podcastDetails["Duration in number of seconds"]
                           ,podcastDetails["Uploaded time"],podcastDetails["Host"],podcastDetails["Participants"])
            else:
                newPodcast = Podcast(podcastDetails["ID"],podcastDetails["Name of the podcast"],podcastDetails["Duration in number of seconds"]
                           ,podcastDetails["Uploaded time"],podcastDetails["Host"])
            response = newPodcast.create()
            return jsonify({"response":response["message"]}),response["code"]
        except:
            return jsonify({"response":"Bad Request"}),400
    elif(param["aduioFileType"]=="audiobook"):
        try:
            audiobookDetails = param["audioFileMetadata"]
            audiobook = AudioBook(audiobookDetails["ID"],audiobookDetails["Duration in number of seconds"]
                           ,audiobookDetails["Uploaded time"],audiobookDetails["Narrator"],audiobookDetails["title"]
                           ,audiobookDetails["Author"])
            response = audiobook.create()
            return jsonify({"response":response["message"]}),response["code"]
        except:
            return jsonify({"response":"Bad Request"}),400

    return jsonify({"response":"field are missing"}),404

@app.route("/delete/<audioFileType>/<audioFileID>")
def delete(audioFileType=None,audioFileID=None):
    if audioFileType is None or audioFileID is None:
        return jsonify({"response":"Bad Request"}),400
   
    if(str(audioFileType)=="song"):
        try:
            response = Song.delete(int(audioFileID))
            return jsonify({"response":response["message"]}),response["code"]
        except:
            return jsonify({"response":"Bad Request"}),400

    elif(str(audioFileType)=="podcast"):
        try:
            response = Podcast.delete(int(audioFileID))
            return jsonify({"response":response["message"]}),response["code"]
        except:
            return jsonify({"response":"Bad Request"}),400
    elif(str(audioFileType)=="audiobook"):
        try:
            response = AudioBook.delete(int(audioFileID))
            return jsonify({"response":response["message"]}),response["code"]
        except:
            return jsonify({"response":"Bad Request"}),400
    return jsonify({"response":"Bad Request"}),400

@app.route("/update/<audioFileType>/<audioFileID>")
def update(audioFileType=None,audioFileID=None):
    if audioFileType is None or audioFileID is None:
        return jsonify({"response":"Bad Request"}),400
    if(str(audioFileType)=="song"):
        try:
            
            param = request.get_json(force=True)
            
            songDetails = param["audioFileMetadata"]

            if(int(audioFileID) != songDetails["ID"]):
                return jsonify({"response":"Bad Request"}),400

            newSong = Song(songDetails["ID"],songDetails["Name of the song"],songDetails["Duration in number of seconds"]
                           ,songDetails["Uploaded time"])

            response=newSong.update(int(audioFileID))
            return jsonify({"response":response["message"]}),response["code"]
        except:
            return jsonify({"response":"Bad Request"}),400    
    elif(str(audioFileType)=="podcast"):
        try:
            
            param = request.get_json(force=True)
            
            podcastDetails = param["audioFileMetadata"]

            if(int(audioFileID) != podcastDetails["ID"]):
                return jsonify({"response":"Bad Request"}),400

            podcastDetails = param["audioFileMetadata"]
            if podcastDetails["Participants"]:
                newPodcast = Podcast(podcastDetails["ID"],podcastDetails["Name of the podcast"],podcastDetails["Duration in number of seconds"]
                           ,podcastDetails["Uploaded time"],podcastDetails["Host"],podcastDetails["Participants"])
            else:
                newPodcast = Podcast(podcastDetails["ID"],podcastDetails["Name of the podcast"],podcastDetails["Duration in number of seconds"]
                           ,podcastDetails["Uploaded time"],podcastDetails["Host"])

            response=newPodcast.update(int(audioFileID))
            return jsonify({"response":response["message"]}),response["code"]
        except:
            return jsonify({"response":"Bad Request"}),400
    elif(str(audioFileType)=="audiobook"):
        try:
            
            param = request.get_json(force=True)
            
            audiobookDetails = param["audioFileMetadata"]

            if(int(audioFileID) != audiobookDetails["ID"]):
                return jsonify({"response":"Bad Request"}),400

            audiobook = AudioBook(audiobookDetails["ID"],audiobookDetails["Duration in number of seconds"]
                           ,audiobookDetails["Uploaded time"],audiobookDetails["Narrator"],audiobookDetails["title"]
                           ,audiobookDetails["Author"])

            response=audiobook.update(int(audioFileID))
            return jsonify({"response":response["message"]}),response["code"]
        except:
            return jsonify({"response":"Bad Request"}),400    
    return jsonify({"response":"Bad request"}),404

@app.route("/get/<audioFileType>/<audioFileID>")
@app.route("/get/<audioFileType>")
@app.route("/get/<audioFileType>/")
def get(audioFileType=None,audioFileID=None):
    
    if audioFileType is None:
        return jsonify({"response":"Bad Request"}),400

    if(str(audioFileType)=="song"):
        try:    
            response= Song.get((audioFileID))
            return jsonify({"response":response["message"]}),response["code"]
        except:
            return jsonify({"response":"Bad Request"}),400    
    elif(str(audioFileType)=="podcast"):
        try:    
            response= Podcast.get((audioFileID))
            return jsonify({"response":response["message"]}),response["code"]
        except:
            return jsonify({"response":"Bad Request"}),400 
    elif(str(audioFileType)=="audiobook"):
        try:    
            response= AudioBook.get((audioFileID))
            return jsonify({"response":response["message"]}),response["code"]
        except:
            return jsonify({"response":"Bad Request"}),400

    return jsonify({"response":"Bad request"}),404

    
if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)

