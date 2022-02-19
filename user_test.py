import unittest
from user import User

class TestUser(unittest.TestCase):
    """
    A test class for the class User which checks for the user details behaviors.
    unittest.TestCase class to help in creating test cases
    """

def setUp(self):
    """
    The set up method is to run before a test case
    """

    self.new_user = User('Brian', 'odhis')

def test_init(self):
    """
    This tests if the object is correctly initialized
    """

    self.assertTrue(self.new_user.username, 'Brian')
    self.assertTrue(self.new_user.user_password, 'odhis')


    

    



