from fastapi import FastAPI

# from base_models import User
# from services.user_service import UserService
import os
app = FastAPI()
# user_service = UserService()


@app.get('/')
def read_root():
    return {"hello": f"from: {os.environ.get('ENV', 'DEFAULT_ENV')}"}

# @app.get('/home')
# def read_root():
#     return {"res": "HelloWorld"}
#
#
# @app.get('/user')
# def read_root():
#
#     return user_service.get_user_data()
#
#
# @app.post('/save-user')
# def read_root(user: User):
#     return user_service.update_user_data(user=user)
