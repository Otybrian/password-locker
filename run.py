from signal import siginterrupt
from user import User
from credentials import Credentials
import random

def create_account(username, user_password):
    """
    Method that helps in creating a user account
    """
    new_user = User(username, user_password)
    return new_user

def main():
    print("Welcome to password locker? Write your name to login")
    username = input()

    print("Hi", + username + "Would you want to sign in or sign up?'\n' For sign in type si'\n' For sign up type su")
    input()

    if input() == "si":
        print("enter your username:")
        username = input()

        print("enter your password")
        user_password = input()

        print("renter password to confirm")
        confirm_password = input()

        while user_password != confirm_password:
            print("entered passwords did not match'\n'Enter password again")
            user_password=input()
            print("renter password to confirm")
            confirm_password = input()

        else:
            print(username + "your account has been created successful")

if __name__=='__main__':
     main()


