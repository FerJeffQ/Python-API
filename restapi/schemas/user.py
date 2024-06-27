from pydantic import BaseModel


# Valores para la creacion de usuario
# {
#     "email": "xW5zY@example.com"
# }
class UserCreate(BaseModel):
    email: str


# Como se devuelve el usuario
# {
#     "id": 1,
#     "email": "xW5zY@example.com"
# }
class User(BaseModel):
    id: int
    email: str
