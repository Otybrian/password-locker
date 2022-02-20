import random
import string
from user import User

class Credentials:

        user_credential_list = []

        @classmethod
        def confirm_user(cls, username, user_password):

            saved_user = ""
            for user in User.user_list:
                if(user.username == username and user.user_password == user_password):
                    saved_user == user.username
            return saved_user
        """
        The method confirm_user determines if the user details entered is in the user_list
        """

        def __init__(self, user_account, user_name, password):
            """
            This method defines the credentials that have been entered by the user to be stored
            """

            self.user_account = user_account
            self.user_name = user_name
            self.password = password

        def save_credentials(self):
            Credentials.user_credential_list.append(self)
            """
            This method is to store a new set of credentials entered by a user by adding them to the 
            user_credential_list
            """

        def delete_user_credentials(self):
            """
            A method that removes user credentials from the user_credential_list
            """
            Credentials.user_credential_list.remove(self)



        @classmethod
        def credentials_available(cls, user_account):
            """
            This method checks whether credentials for the user_account details entered exists in the 
            user_credential_list
            """
            for credential in cls.user_credential_list:
                if credential.user_account == user_account:
                    return True
            return False

    
        @classmethod 
        def access_credentials(cls, user_account):
            """
            This method helps user find their credentials by taking in a user's user_account name
            and returns the credential details that matches the user_account name entered
            """

            for credential in cls.user_credential_list:
                if credential.user_account == user_account:
                    return credential

       