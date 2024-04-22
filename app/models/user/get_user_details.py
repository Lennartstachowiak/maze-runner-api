from db.models import Users


def get_user_details(user: Users):
    user_details = {
        "id": user.id,
        "email": user.email,
    }
    return user_details
