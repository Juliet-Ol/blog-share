
import unittest
from models import User

User = User.user

class UserTest(unittest.TestCase):
    def setUp(self):
        self.new_user = User("id","username","email","password")

    def test_init(self):
        self.assertEqual(self.new_user,"id")
        self.assertEqual(self.new_user,"username")
        self.assertEqual(self.new_user,"email")
        self.assertEqual(self.new_user,"password")


if __name__=='__main':
    unittest.main()