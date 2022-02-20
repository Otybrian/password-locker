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

        self.assertEqual(self.new_user.username, 'Brian')
        self.assertEqual(self.new_user.user_password, 'odhis')

    def test_save_user(self):
        """
        Method tests if a new user instance has been  added to the user_list
        """

        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)

    def test_show_user_details(self):
        """
        This test-case tests if a new user instance has been added to the user_list
        """

        self.new_user.show_user_details()
        self.assertEqual(len(User.user_list),1)


    def tearDown(self):
        """
        Testcase cleans up after each testcase has run
        """
        User.user_list = []

if __name__ == "__main__":
    unittest.main()





    



