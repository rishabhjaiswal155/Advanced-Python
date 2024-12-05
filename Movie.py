#Creating list of Objects
class Movie:
	def __init__(self,name,actor,actress,rating):
		self.name=name
		self.actor=actor
		self.actress=actress
		self.rating=rating
	def info(self):
		print("Movie Name is:",self.name)
		print("Actor Name is:",self.actor)
		print("Actress Name is:",self.actress)
		print("Movie rating is:",self.rating)
		print()
movies=[Movie('Bahubali','Prabhas','Anushka S.',9.5),
        Movie('KGF','Yash','Raveena',8.5),
        Movie('Don','Shahrukh','Priyanka',6.5),
        Movie('Brahmastra','Ranbir','Alia',7.5)]
for movie in movies:
	movie.info()
	