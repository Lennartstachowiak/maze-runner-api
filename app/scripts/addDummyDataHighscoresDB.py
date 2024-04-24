from api import create_api
from db.models import Highscores, Users, Mazes, Algorithms
import random

api = create_api()
api.app_context().push()

all_user_ids = []
for user in Users.query.all():
    all_user_ids.append(user.id)

all_maze_ids = []
for maze in Mazes.query.all():
    all_maze_ids.append(maze.id)

dummyHighscore = []

for maze_id in all_maze_ids:
    for user_id in all_user_ids:
        first_algorithm_id = Algorithms.query.filter_by(user_id=user_id).first().id
        random_score = random.randint(0, 1000)
        dummyHighscore.append(
            {
                "user_id": user_id,
                "maze_id": maze_id,
                "score": random_score,
                "algorithm_id": first_algorithm_id,
            }
        )


for highscore in dummyHighscore:
    new_highscore = Highscores(
        user_id=highscore["user_id"],
        maze_id=highscore["maze_id"],
        score=highscore["score"],
        algorithm_id=highscore["algorithm_id"],
    )
    new_highscore.save()
