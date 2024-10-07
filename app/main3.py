from fastapi import FastAPI
from fastapi import status
from fastapi.responses import JSONResponse

from base_models import User2
from services.greet_service import GreetService

app = FastAPI()
greet_service = GreetService()


@app.get("/")
def route():
    return {"hello": "world1"}


@app.get("/get-greet")
def get_username():
    return greet_service.get_user_name()


@app.post("/update-greet")
def update_username(user: User2):
    if user.name is None or user.name is "":
        return JSONResponse(content="name is empty", status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)
    return greet_service.update_user_name(user=user)
