from db import models

User = models.User
Highscores = models.Highscores


def get_highscores(maze_id):
    highscores = Highscores.query.filter_by(mazeId=maze_id)
    highscoreList = []
    for highscore in highscores:
        user_email = User.query.filter_by(
            id=highscore.userId).first().email
        highscoreList.append(
            {"name": user_email, "score": highscore.score})
    return highscoreList
