import unittest
from Classes.User import User


class TestUser(unittest.TestCase):
    def test_init_user(self):
        user_obj = User("John", 3, 'john@gmail', 'pass1')
        self.assertEqual(user_obj.name, "John")
        self.assertEqual(user_obj.user_id, 3)
        self.assertEqual(user_obj.email, 'john@gmail')
        self.assertEqual(user_obj.password, 'pass1')


if __name__ == '__main__':
    unittest.main()
