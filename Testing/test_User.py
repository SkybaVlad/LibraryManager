import unittest
from Classes.User import User

class TestUser(unittest.TestCase):
    def init_user(self):
        user_obj = User("John",3)
        self.assertEqual(user_obj.name, "John")
        self.assertEqual(user_obj.user_id,3)