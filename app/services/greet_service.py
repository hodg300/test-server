class GreetService:
    username = ""

    def update_user_name(self, user):
        self.username = user.name
        print(f"update_user_name - {self.username}")
        return {"name": self.username}

    def get_user_name(self):
        print(f"get_user_name - {self.username}")
        return {"name": self.username}
