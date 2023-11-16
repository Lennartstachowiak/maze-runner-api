from db import models

User = models.Users
Algorithms = models.Algorithms
Highscores = models.Highscores


def create_highscores_object_list(highscores):
    highscoreList = []
    for highscore in highscores:
        user_email = User.query.filter_by(
            id=highscore.userId).first().email
        algorithm_name = Algorithms.query.filter_by(
            id=highscore.algorithm_id).first().name
        highscoreList.append(
            {"name": user_email, "algorithm_name": algorithm_name, "score": highscore.score})
    return highscoreList
