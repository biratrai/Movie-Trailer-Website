import webbrowser

class Movie(object):
	""" This class provides a way to store movie related information"""

	# A list for storing the VALID_RATINGS
	VALID_RATINGS = ["G", "PG", "PG-13", "R"]

	# Movie Constructor 
	def __init__(self, movie_title, movie_image, movie_story, movie_url):
		''' 
			Initialize the Movie object and set the values 
			movie_title, movie_image, movie_story, movie_url

		'''
		self.title = movie_title
		self.poster_image_url = movie_image
		self.story_line = movie_story
		self.trailer_youtube_url = movie_url

	# Function to open browser with youtube trailer
	def show_trailer(self):
		""" Open the browser through webbrowser function imported from webbrowser module"""
		webbrowser.open(self.trailer_youtube_url)