from flask import make_response
from db import models
from services.user.logout_user import logout_user


def logout_user_controller(request):
    session_id = request.cookies.get('sessionId')
    is_logged_out = logout_user(session_id)
    if is_logged_out:
        res = make_response()
        res.delete_cookie('sessionId')
        return res
