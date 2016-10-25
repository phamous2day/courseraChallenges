from user import User
import json

user = User("Dave")

user.add_movie("The Martian", "Sci-fi")
user.add_movie("Star Trek Beyond", "Action")

print(user.json())

with open('my_file.txt', 'w') as f:
    json.dump(user.json(), f)