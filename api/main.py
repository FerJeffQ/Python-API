from fastapi import Depends, FastAPI, Header, HTTPException, status

app = FastAPI()


def secret_header(secretHeader: str | None = Header(None)) -> None:
    if not secretHeader or secretHeader != "SECRET_VALUE":
        raise HTTPException(status.HTTP_403_FORBIDDEN)


@app.get("/protected-route", dependencies=[Depends(secret_header)])
async def protected_route():
    return {"hello": "world"}
