from app.models.user.get_user_details import get_user_details
from app.models.user.get_user import get_user_by_id
from db.models import Users, UserFollowers


def get_user_followers(user: Users):
    user_followers = (
        Users.query.join(UserFollowers, Users.id == UserFollowers.followerId)
        .filter(UserFollowers.userId == user.id)
        .all()
    )
    follower_list = []
    for user_follower in user_followers:
        user_follower_id = user_follower.id
        user_follower = get_user_by_id(user_follower_id)
        follower_user = get_user_details(user_follower)
        follower_list.append(follower_user)
    return follower_list
