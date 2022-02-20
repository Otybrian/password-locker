import unittest
from credentials import Credentials


class TestCredentials(unittest.TestCase):
    """
    Test class that defines test cases for the class Credentials
    """

    def setUp(self):
        """
        This method runs before each individual test for credentials run
        """

        self.new_credential = Credentials('twitter', 'otbrayo', 'comE@5on')

    def test_init(self):
        """
        A test case that checks whether a new instance of Credentials has been 
        correctly initialized
        """
        self.assertEqual(self.new_credential.user_account, 'twitter')
        self.assertEqual(self.new_credential.user_name, 'otbrayo')
        self.assertEqual(self.new_credential.password, 'comE@5on')

    def save_credentials_test(self):
        """
        This testcase tests whether credential object is successfully saved/ appended 
        into the user_credential_list
        """

        self.new_credential.save_credentials()
        self.assertEqual(len(Credentials.user_credential_list),1)

    def delete_user_credentials_test(self):
        """
        This testcase tests whether credential object is successfully deleted/ removed 
        from the user_credential_list
        """

        self.new_credential.delete_user_credentials()
        self.assertEqual(len(Credentials.user_credential_list),0)
