from fastapi import APIRouter, HTTPException, status

from api.db import db

from api.schemas.user import User, UserCreate

router = APIRouter()


@router.get("/")
async def all() -> list[User]:
    return list(db.users.values())


@router.get("/{user_id}")
async def get(user_id: int) -> User:
    try:
        return db.users[user_id]
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create(user_create: UserCreate) -> User:
    new_id = max(db.users.keys() or (0,)) + 1
    user = User(id=new_id, **user_create.model_dump())
    db.users[new_id] = user
    return user


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(user_id: int) -> None:
    try:
        db.users.pop(user_id)
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
