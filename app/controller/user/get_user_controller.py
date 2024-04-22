from app.models.user.get_user import get_user_by_id
from app.models.user.get_user_details import get_user_details


def get_user_controller(request):
    user_id = request.args.get("id")
    user = get_user_by_id(user_id)
    res = get_user_details(user)
    return res
