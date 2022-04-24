import unittest
from passlock import User


class TestUser(unittest.TestCase):
    """
    Test class that defines  test cases for the user class behaviours.

    Args:
    unittest.Testcase: TestCase class that helps in creating test cases
    """

    def setUp(self):
        """
        Set up method to run before each test cases
        """
        self.new_user = User("Meshack Cheberi", "Meshack011")

    def save_user(self):
        """
        saves a new user to user list
        """

        User.user_list.append(self)

    @classmethod
    def get_user(cls):
        return cls.user_list

    def delete_user(self):
        """
        delete a saved account from the user list
        """
        User.user_list.remove(self)
