from api.schemas.user import User


class DB:
    users: dict[int, User] = {}


db = DB()
