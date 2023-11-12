from flask import make_response
from app.models.user.logout_user import logout_user


def logout_user_controller(request):
    session_id = request.cookies.get('session_id_maze_runner')
    is_logged_out = logout_user(session_id)
    if is_logged_out:
        res = make_response()
        res.delete_cookie('session_id_maze_runner')
        return res
