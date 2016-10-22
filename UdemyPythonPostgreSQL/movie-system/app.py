# from movie import Movie
# from user import User
#
# user = User("Dave")
# my_movie = Movie("The Martian", "Action", True)
#
# user.movies.append(my_movie)
#
#
# print(user.watched_movies())

# with open('my_file.txt', 'w') as f:
#     print(f.readline())

from user import User

user = User("Dave")

user.add_movie("The Martian", "action")
user.add_movie("Zootopia", "animation")

user.save_to_file()