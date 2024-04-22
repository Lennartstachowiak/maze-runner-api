from sqlalchemy.exc import IntegrityError
from db import models
from db.db import db

UserFollowers = models.UserFollowers


def follow_user(user_id, user_id_followed):
    try:
        new_follow = UserFollowers(userId=user_id_followed, followerId=user_id)
        db.session.add(new_follow)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return 409
