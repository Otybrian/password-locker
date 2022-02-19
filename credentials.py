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

        @classmethod 
            

