from media import Media

class Series(Media) :
    def __init__(self, number_of_episodes, broadcast_method) :
      super().__init__()
      self.number_of_episodes=number_of_episodes
      self.broadcast_method=broadcast_method
