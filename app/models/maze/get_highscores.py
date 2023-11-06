from db import models

User = models.Users
Algorithms = models.Algorithms
Highscores = models.Highscores


def get_highscores(maze_id):
    highscores = Highscores.query.filter_by(mazeId=maze_id)
    highscoreList = []
    for highscore in highscores:
        user_email = User.query.filter_by(
            id=highscore.userId).first().email
        algorithm_name = Algorithms.query.filter_by(
            id=highscore.algorithm_id).first().name
        highscoreList.append(
            {"name": user_email, "algorithm_name": algorithm_name, "score": highscore.score})
    return highscoreList
