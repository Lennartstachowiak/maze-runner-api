from app.controller.maze.add_maze_highscore import add_maze_highscore
from app.controller.maze.remove_maze_highscore import remove_maze_highscore
from db.models import Highscores


def handle_adding_maze_highscore(user_id, maze_id, algorithm_id, solution):
    new_score = solution["score"]
    user_highscore_list = Highscores.query.filter_by(
        mazeId=maze_id, userId=user_id).all()
    user_highscores = [vars(record) for record in user_highscore_list]
    best_highscore = min(
        user_highscores, key=lambda user_highscore: user_highscore["score"])
    old_score = best_highscore["score"]
    for highscore in user_highscores:
        if highscore["id"] is best_highscore["id"]:
            continue
        highscore_id = highscore["id"]
        remove_maze_highscore(highscore_id)
    if new_score > old_score:
        return
    add_maze_highscore(user_id, maze_id, algorithm_id, solution)
