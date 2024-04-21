# Can be added to user profiles

from db.models import Highscores, Users, Mazes, Algorithms


def get_user_highscores(user_id):
    highscores = Highscores.query \
        .join(Users, Highscores.userId == Users.id) \
        .join(Mazes, Highscores.mazeId == Mazes.id) \
        .join(Algorithms, Highscores.algorithm_id == Algorithms.id) \
        .filter(Highscores.userId == user_id) \
        .all()
    highscoreList = []
    for highscore in highscores:
        highscoreList.append(
            {"name": highscore.user.email, "algorithm_name": highscore.algorithm.name, "score": highscore.score, "maze": highscore.maze.name})
    return highscores
