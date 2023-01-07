from media import Media
from media import Actor
class Clip(Media):
 def __init__(self, id, name, director, imdb, url, duration, casts, genre, writer):
        super().__init__()
        self.id=id
        self.name=name
        self.director=director
        self.imdb=imdb
        self.url=url
        self.duration=duration
        self.casts=casts
        self.genre=genre
        self.writer=writer









