import media
import fresh_tomatoes

# Populating the Movie object with data
boy_hood = media.Movie("Boy Hood", 
	"http://upload.wikimedia.org/wikipedia/en/b/bb/Boyhood_film.jpg",
	"Filmed over 12 years with the same cast, Richard Linklater's BOYHOOD is a groundbreaking story of growing up as seen through the eyes of a child named Mason (a breakthrough performance by Ellar Coltrane), who literally grows up on screen before our eyes."
	,"https://www.youtube.com/watch?v=Y0oX0xiwOv8")

forrest_gump = media.Movie("Forrest Gump",
	"http://upload.wikimedia.org/wikipedia/en/6/67/Forrest_Gump_poster.jpg",
	"Forrest Gump is a simple man with a low I.Q. but good intentions. He is running through childhood with his best and only friend Jenny. His 'mama' teaches him the ways of life and leaves him to choose his destiny.",
	"https://www.youtube.com/watch?v=bLvqoHBptjg")

frozen = media.Movie("Frozen",
	"http://upload.wikimedia.org/wikipedia/en/0/05/Frozen_%282013_film%29_poster.jpg",
	"After the kingdom of Arendelle is cast into eternal winter by the powerful Snow Queen Elsa, her sprightly sister Anna teams up with a rough-hewn mountaineer named Kristoff (Jonathan Groff) and his trusty reindeer Sven to break the icy spell",
	"https://www.youtube.com/watch?v=FLzfXQSPBOg")

into_the_wild = media.Movie("Into The Wild",
	"http://upload.wikimedia.org/wikipedia/en/8/8a/Into-the-wild.jpg",
	"A young man leaves his middle class existence in pursuit of freedom from relationships and obligation. Giving up his home, family, all possessions but the few he carried on his back, and donating all his savings to charity, Christopher McCandless (Emile Hirsch) embarks on a journey throughout America. His eventual aim is to travel into Alaska, into the wild, to spend time with nature, with 'real' existence, away from the trappings of the modern world.",
	"https://www.youtube.com/watch?v=g7ArZ7VD-QQ")

iron_man = media.Movie("Iron Man",
	"http://upload.wikimedia.org/wikipedia/en/7/70/Ironmanposter.JPG",
	"Tony Stark. Genius, billionaire, playboy, philanthropist. Son of legendary inventor and weapons contractor Howard Stark. He survives - barely - with a chest full of shrapnel and a car battery attached to his heart.Thus Iron Man is born. ",
	"https://www.youtube.com/watch?v=8hYlB38asDY")

furious_7 = media.Movie("Furious 7",
	"http://upload.wikimedia.org/wikipedia/en/b/b8/Furious_7_poster.jpg",
	"Deckard Shaw seeks revenge against Dominic Toretto and his family for the death of his brother.After learning of Han's death, the crew sets out to find the man who killed one of their own, before he finds them first.",
	"https://www.youtube.com/watch?v=4vYQby_hDDU")

# Creating movies array from the populated Movie object
movies = [boy_hood,forrest_gump,frozen,into_the_wild,iron_man,furious_7]

# Call to the open_movies_page() function inside fresh_tomatoes module
fresh_tomatoes.open_movies_page(movies)

