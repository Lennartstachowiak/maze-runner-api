from app.models.user.get_user_details import get_user_details
from app.models.user.get_user import get_user_by_id
from db.models import Users, UserFollowers


def get_user_following(user: Users):
    user_follows = (
        Users.query.join(UserFollowers, Users.id == UserFollowers.user_id)
        .filter(UserFollowers.follower_id == user.id)
        .all()
    )
    following_list = []
    for user_follow in user_follows:
        user_follow_id = user_follow.id
        user_follow = get_user_by_id(user_follow_id)
        following_user = get_user_details(user_follow)
        following_list.append(following_user)
    return following_list
