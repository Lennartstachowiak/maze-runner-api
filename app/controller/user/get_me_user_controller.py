from app.models.user.get_user import get_user
from app.models.user.get_user_details import get_user_details


def get_me_user_controller(request):
    user = get_user(request)
    res = get_user_details(user)
    return res
