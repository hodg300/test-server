from app.base_models import User


class UserService:

    username = None
    age = None

    def update_user_data(self, user: User):
        if user.username is None and user.age is None:
            print("username and age contain None values")
            return
        print(f"{user.username=}, {user.age=}")
        self.username = user.username
        self.age = user.age
        return {"username": self.username, "age": self.age}

    def get_user_data(self):
        print(f"${self.username}, {self.age}")
        if self.username is None or self.age is None:
            return {"username": "SampleUser", "age": 30}
        return {"username": self.username, "age": self.age}
