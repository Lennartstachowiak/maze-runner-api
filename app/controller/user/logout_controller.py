from flask import make_response
from app.controller.user.remove_session_controller import remove_session_controller
from db.models import SessionAuth


def logout_user_controller(request):
    session_id = request.cookies.get('session_id_maze_runner')
    delete_session = SessionAuth.query.get(session_id)
    remove_session_controller(delete_session)
    if delete_session:
        res = make_response()
        res.delete_cookie('session_id_maze_runner')
        return res
