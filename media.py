import webbrowser

class Video():
    def __init__(self, title):
        self.title = title
#        self.duration = duration
    def show_info(self):
        print("Title - "+self.title)

class Movie(Video):
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    
    def __init__(self, title, movie_storyline, poster_image, trailer_youtube):
        Video.__init__(self, title)
        self.title = title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

#class TvShow(Video):
#    def __init__(self, show_title, show_season,  show_episode, show_network)
#        Video.__init__(self, title)
#       self.title = title
#        self.season = show_season
#        self.episode = show_episode
#        self.network = show_network

#    def get_local_listing()
