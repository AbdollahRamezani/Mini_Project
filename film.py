from media import Media
class Film(Media):
    def __init__(self, genre, grimmour, sunic):
        super().__init__()
        self.genre=genre
        self.grimmour=grimmour
        self.sunic=sunic