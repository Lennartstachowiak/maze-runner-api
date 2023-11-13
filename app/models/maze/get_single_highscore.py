from db.models import Highscores


def get_single_highscore(highscore_id):
    highscore = Highscores.query.filter_by(id=highscore_id).first()
    return highscore
