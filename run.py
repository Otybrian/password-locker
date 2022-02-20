from signal import siginterrupt
from user import User
from credentials import Credentials
import random

def main():
    print("Welcome to password locker? Write your name to login")
    username = input()

    print("Hi", + username + "Would you want to sign in or sign up?\n For sign in type si\n For sign up type su")
    input()

    if input() == "si":
        print("enter your username:")
        username = input()

        print("enter your password")
        password = input()

        print("renter password to confirm")
        confirm_password = input()

        while password != confirm_password:
            print("entered passwords did not match\nEnter password again")
            password=input()

