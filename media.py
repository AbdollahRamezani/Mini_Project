import pytube
class Media():
    def __init__(self):
        self.id=None
        self.name=None
        self.director=None
        self.imdb=None
        self.url=None
        self.duration=None
        self.casts=None

    def showInfo (self):
        ...

    def download (self, url, clip_name):
      self.link=url
      self.clip_name=clip_name
      first_stream=pytube.YouTube(self.link).streams.first()
      first_stream.download(output_path='./' , filename=self.clip_name+".mp4")
 
  

class Actor():
    def __init__(self, id, actor_name, media_id):
         self.id=id
         self.actor_name=actor_name
         self.media_id=media_id
         





