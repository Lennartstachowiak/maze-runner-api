from db.models import Highscores, Users, Algorithms


def get_maze_highscores(maze_id):
    highscores = (
        Highscores.query.join(Users, Highscores.user_id == Users.id)
        .join(Algorithms, Highscores.algorithm_id == Algorithms.id)
        .filter(Highscores.maze_id == maze_id)
        .all()
    )
    highscoreList = []
    for highscore in highscores:
        highscoreList.append(
            {
                "user_id": highscore.user.id,
                "name": highscore.user.email,
                "algorithm_name": highscore.algorithm.name,
                "score": highscore.score,
            }
        )
    return highscoreList
