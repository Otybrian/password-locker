from user import User
from credentials import Credentials

def create_account(username, user_password):
    """
    Method that helps in creating a user account
    """
    new_user = User(username, user_password)
    return new_user

def save_user(user):
    """
    method that saves a user
    """

    User.save_user(user)

def find_user(name):
    """
    Method checks if a user account name already exists
    """

    return User.confirm_user(name)

def user_sign_in(username, user_password):
    """
    Allows user to sign into their account
    """

    sign_in=User.sign_in(username, user_password)
    if sign_in !=False:
        return User.sign_in(username, user_password)

def create_credentials(user_account, user_name, password):
    """Method creates a new credential
    """

    new_credential = Credentials(user_account, user_name, password)

    return new_credential

def save_credential(user_account):

    """
    Function to save credential
    """

    Credentials.save_credentials(user_account)

def generated_password():
    """
    Method that generates password for the user
    """

    password = Credentials.passwordGenerator()

    return password




def main():
    """
    Function runs the password-locker
    """
    print("Welcome to password locker? Write your name to login")
    username = input()
     
    while True:
        """
        Loop runs in the whole application
        """


        print("""short_codes:
        For sign-in - si \n
        To display users - si \n
        generate password - gp""")
        short_code = input().lower()

        if short_code == "si":

            """
            signing in
            """
        print("enter your username:")
        username = input()

        print("enter your password")
        user_password = input()

        print("renter password to confirm")
        confirm_password = input()

        if user_password != confirm_password:
            print("entered passwords did not match'\n'Enter password again")
            user_password=input()
            print("renter password to confirm")
            confirm_password = input()

        
            """
            create and save new user
            """
            save_user(create_account(username, user_password))
            print(username + " , " " your account has been created successful")
            print('\n')
            print("To find existing credentials type: su")


        elif short_code == 'su':

            """
            Show names of exisiting users
            """
            print("Here is a list of existing users")

            if find_user():
                print("List of existing user credentials")

                for username in find_user():
                    print('your username is ' + username + ' your password is ' + user_password)

            else:
                print("\n")
                print("There are no existing users")


        elif short_code == "gp":
            """
            generates password for users
            """

if __name__=='__main__':
     main()


