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

        