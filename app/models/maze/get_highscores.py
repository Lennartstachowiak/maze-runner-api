from db.models import Highscores


def get_highscores(maze_id):
    highscores = Highscores.query.filter_by(mazeId=maze_id)
    return highscores
