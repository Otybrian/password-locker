class User:
    """
    Creating a class and calling it User. The class will be generating new instances of a user.
    """
    user_list = []
    """
    An empty list called user_list will store the user details
    """
    def _init_(self, username, user_password):
        self.username = username
        self.user_password = user_password
        """
        This method defines a user's properties
        """

    def _init_(self):
        User.user_list.append(self)

        """
        The method that will save a new user by adding their details to the user_list
        """

    @classmethod
    def show_user_details(cls):
        return cls.user_list


    def remove_user_details(self):

        User.user_list.remove(self)

        """
        A classmethod decorator to declare class methods to display and 
        remove user details
        """

    class Credentials:

        user_credential_list = []

        @classmethod
        def confirm_user(cls, username, user_password):

            saved_user = ""
            for user in User.user_list:
                if(user.username == username and user.user_password == user_password):
                    saved_user == user.username
            return saved_user