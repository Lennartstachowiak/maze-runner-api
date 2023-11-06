
from api import create_api
from db.models import Highscores, Users, Mazes
import random

api = create_api()
api.app_context().push()

allUserIds = []
for user in Users.query.all():
    allUserIds.append(user.id)

allMazeIds = []
for maze in Mazes.query.all():
    allMazeIds.append(maze.id)

dummyHighscore = []

for mazeId in allMazeIds:
    for userId in allUserIds:
        random_score = random.randint(0, 1000)
        dummyHighscore.append(
            {"userId": userId, "mazeId": mazeId, "score": random_score})


for highscore in dummyHighscore:
    new_highscore = Highscores(userId=highscore["userId"], mazeId=highscore["mazeId"],
                               score=highscore["score"])
    new_highscore.save()
