from db.models import Highscores


def remove_maze_highscore(highscore_id):
    highscore = Highscores.query.filter_by(id=highscore_id).first()
    highscore.delete()
