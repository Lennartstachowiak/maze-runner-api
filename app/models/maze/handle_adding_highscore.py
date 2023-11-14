from app.controller.maze.add_maze_highscore import add_maze_highscore_controller
from app.controller.maze.remove_maze_highscore import remove_maze_highscore_controller
from db.models import Highscores


def handle_adding_maze_highscore(user_id, maze_id, algorithm_id, solution):
    user_highscore_list = Highscores.query.filter_by(
        mazeId=maze_id, userId=user_id).all()
    user_highscores = []
    for user_highscore_object in user_highscore_list:
        user_highscore_dict = {
            "id": user_highscore_object.id, "score": user_highscore_object.score}
        user_highscores.append(user_highscore_dict)

    if (len(user_highscores) == 0):
        add_maze_highscore_controller(user_id, maze_id, algorithm_id, solution)
        return

    best_highscore = min(
        user_highscores, key=lambda user_highscore: user_highscore["score"])

    for highscore in user_highscores:
        if highscore["id"] is best_highscore["id"]:
            continue
        highscore_id = highscore["id"]
        remove_maze_highscore_controller(highscore_id)

    old_score = best_highscore["score"]
    new_score = solution["score"]
    if new_score < old_score:
        add_maze_highscore_controller(user_id, maze_id, algorithm_id, solution)
        remove_maze_highscore_controller(best_highscore["id"])
