#!/usr/bin/env python3
from password import Credential
from password import userInfomation
import random
import string
import time
import pyperclip

def create_credentials(user_name, email, password):
    '''
    function that creates new credentials
    '''
    new_credential = Credential(user_name,email, password)
    return new_credential

def save_credentials(credential):
    '''
    function that saves credentials
    '''
    credential.save_credentials()


def find_existing_credentials(user_name):
    '''
    function to test if credentials exist
    '''
    return Credential.credentials_exist(user_name)

def find_existing_credentials(email):
    '''
    function to test if credentials exist
    '''
    return Credential.credentials_exist(email)
    

def authenticate_credentials(user_name, email,password):
    '''
    '''
    return Credential.authenticate_credentials(user_name,password)

def user_information(account_name,account_user_name, account_email, account_password):
    '''
    Function to authenticate and log in a user
    '''
    information = UserInformation(account_name, account_user_name, account_email, account_password)
    return information 

def create_new_information(myinformation):
    '''
    Function that creates new information to save user password
    '''
    myinformation.create_password()


def display_information():
    '''
    function to display the user information
    '''
    return UserInformation.show_user_information()


def information_exist(account_name):
    '''
    Function to check if the information exists
    '''
    return userInfomation.information_exists(account_name)


def find_user_information(account_name):
        '''
        function that finds the user credential information by account_name
        '''

        return UserInformation.find_by_account_name(account_name)


def create_password(password_length):
    '''
    Function that creates a new password
    '''

    password_list = []
    created_password = random.sample(string.ascii_lowercase + string.digits + string.ascii_uppercase,password_length)
    password_list.append(''.join(created_password))
    return password_list


def main():
        print("Hello, welcome to password locker!, What is your name?")
        user_name = input('Name:')
        print(f'hello {user_name}. what would you like to do?')
        print('\n')
        while True:
            print("Use the following short short codes : cc - create a new account, lg - log in , ex - exit")
            short_code = input().lower()

            if short_code == 'cc':
                            print("New Account")
                            print("-"*10)

                            print ("username ....")
                            user_name = input()

                            print("password ...")
                            password = input()
                            save_credentials(create_credentials(user_name,email,password)) # create and save credentials
                            print ('\n')
                            print(f"Your new account with user_name : '{user_name}' email '{email}' and password '{password}' has been created")
                            print ('\n')


            elif short_code == "lg":
                            print("Enter user_name, email and password to login:")
                            print("-"*60)
                            user_name = input("User_name: ")
                            password = input("Password: ")
                            log_in = authenticate_credentials(user_name, email, password)
                            if log_in==0:
                                print("\n")
                                print("Invalid username and/or password")
                                print("-"*30)
                            elif log_in!=0:
                                print("\n")
                                print(f"Welcome {log_in.user_name}! What would you like to do?")
