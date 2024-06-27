from restapi.schemas.user import User


class DummyDatabase:
    users: dict[int, User] = {}


db = DummyDatabase()
