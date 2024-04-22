from db import models

User = models.Users


def search_users(email):
    users = User.query.filter(User.email.ilike(f"%{email.lower()}%")).all()
    return users
