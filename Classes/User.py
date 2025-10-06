class User:
    def __init__(self, name, user_id, email, password):
        self.name = name
        self.user_id = user_id
        self.email = email
        self.password = password

    def __eq__(self, other):
        if isinstance(other, User):
            if self.user_id == other.user_id:
                if self.name == other.name:
                    return True
        return False

    def __hash__(self):
        return hash(self.user_id)
