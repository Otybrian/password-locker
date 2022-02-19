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
