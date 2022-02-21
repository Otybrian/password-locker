import unittest
from user import User
from credentials import Credentials

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

    def tearDown(self):
        """
        Testcase cleans up after each testcase has run
        """
        User.user_list = []

    def test_init(self):
        """
        This tests if the object is correctly initialized
        """

        self.assertEqual(self.new_user.username, 'Brian')
        self.assertEqual(self.new_user.user_password, 'odHis3@1')


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

    def test_sign_in(self):
        """
        Method tests if a user is able to sign into their account
        """

        self.new_user.save_user()
        test_user = User("Brian","odHis3@1")
        test_user.save_user()

        found_credentials = User.sign_in("Brian","odHis3@1")

        self.assertEqual(found_credentials, Credentials.user_credential_list)


  

if __name__ == "__main__":
    unittest.main()





    



