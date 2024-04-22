from app.models.user.search_users import search_users
from app.models.user.get_user_details import get_user_details
from flask import jsonify


def search_user_controller(request):
    email = request.json.get("email")
    users = search_users(email)
    user_details_list = []
    for user in users:
        user_details = get_user_details(user)
        user_details_list.append(user_details)
    return jsonify(user_details_list)
