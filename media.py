import webbrowser

class Movie():
	""" This class provides a way to store movie related information"""
	VALID_RATINGS = ["G", "PG", "PG-13", "R"]

	# Movie Consturctor 
	def __init__(self, movie_title, movie_image, movie_story, movie_url):
		self.title = movie_title
		self.poster_image_url = movie_image
		self.story_line = movie_story
		self.trailer_youtube_url = movie_url

	# Function to open browser with youtube trailer
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)