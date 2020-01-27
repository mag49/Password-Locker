#!/usr/bin/env python3
from password import Credential
from password import UserData
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
    

def authenticate_credentials(user_name, password):
    '''
    '''
    return Credential.authenticate_credentials(user_name,password)

def user_data(account_name,account_user_name, account_email, account_password):
    '''
    Function to authenticate and log in a user
    '''
    information = UserData(account_name, account_user_name, account_email, account_password)
    return data 

def create_new_data(mydata):
    '''
    Function that creates new information to save user password
    '''
    mydata.create_password()


def display_data():
    '''
    function to display the user information
    '''
    return UserData.show_user_data()


def information_exist(account_name):
    '''
    Function to check if the information exists
    '''
    return UserData.information_exists(account_name)


def find_user_data(account_name):
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
            email = input("email...\n")
            save_credentials(create_credentials(user_name,email,password)) # create and save credentials
            print ('\n')
            print(f"Your new account with user_name : '{user_name}' email '{email}' and password '{password}' has been created")
            print ('\n')


        elif short_code == "lg":
            print("Enter user_name and password to login:")
            print("-"*60)
            user_name = input("User_name: ")
            password = input("Password: ")
            log_in = authenticate_credentials(user_name, password)
            if log_in==0:
                print("\n")
                print("Invalid user_name and/or password")
                print("-"*30)
            elif log_in!=0:
                print("\n")
                print(f"Welcome {log_in.user_name}! What would you like to do?")

    while True:
        print("Use the following short short codes : ad - add new password, cp - copy a  password , lp - view you passwords, ex - exit")
        short_code= input()  
        if short_code== "ad":
            print("Enter account name such as facebook, instagram or Gmail:.......")
            account_name = input()
            print(f"Enter user_name account for {account_name}.......")
            account_username = input()
            print("What is you preferred password length?")
            password_length = int(input("Password length:"))
            account_password = create_password(password_length)
            create_new_data(user_data(account_name, account_username, account_password))
            print("\nWait a minute....")
            time.sleep(1.0)
            print("\n")
            print(f"Created  password for {account_name} is {account_password}")
            print(".."*10)

        elif short_code =="cp":
            print("Enter the account name of  password you want to copy")
            get_name = (input("account name : "))
            if information_exist(get_name):
                pyperclip.copy(account_password)
                print("\n")
                print(f"Password for  {account_name} successfully copied to clipboard, go ahead and paste it")
            else:
                print("your password does not exist")
                print("--"*10)



        elif short_code == "lp":
            if show_data():
                print('\n')
            for data in  show_data():
                print(f"{data.account_name}------> {data.account_password}")
                print('\n')

        elif short_code == "ex":
            print(f"Bye{log_in.user_name}")

if __name__ == '__main__':

    main()
