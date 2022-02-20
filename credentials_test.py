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

    def test_save_credentials(self):
        """
        This testcase tests whether credential object is successfully saved/ appended 
        into the user_credential_list
        """

        self.new_credential.save_credentials()
        self.assertEqual(len(Credentials.user_credential_list),1)

    def test_delete_user_credentials(self):
        """
        This testcase tests whether credential object is successfully deleted/ removed 
        from the user_credential_list
        """

        self.new_credential.delete_user_credentials()
        self.assertEqual(len(Credentials.user_credential_list),0)

    def test_credentials_available(self):
        """
        Test case that confirms if the user credentials entered exists in the user_credentials_list
        by taking the user_account and displaying the credentials
        """

        self.new_credential.credentials_available()
        test_credentials_available = Credentials('twitter')
        test_credentials_available.credentials_available()

        self.assertEqual(test_credentials_available.user_credential_list)

