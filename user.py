from credentials import Credentials

class User:
    """
    Creating a class and calling it User. The class will be generating new instances of a user.
    """
    user_list = []
    """
    An empty list called user_list will store the user details
    """
    def __init__(self, username, user_password):
        self.username = username
        self.user_password = user_password
        """
        This method defines a user's properties
        """

    def save_user(self):
        User.user_list.append(self)

        """
        The method that will save a new user by adding their details to the user_list
        """
    
    @classmethod
    def confirm_user(cls, username):
        """
        The method confirm_user determines if the user details entered is in the user_list
        """
        for user in cls.user_list:
            if user.username == username:
                return True

        return False

            

    @classmethod
    def show_user_details(cls):
        """
        Method that displays user list
        """
        return cls.user_list

    @classmethod
    def sign_in(cls, username, user_password):
        """
        Method that will allow user to sign into their account
        """

        for user in cls.user_list:
            if user.username == username and user.user_password == user_password:
                return Credentials.user_credential_list

            
            return False
        
        
