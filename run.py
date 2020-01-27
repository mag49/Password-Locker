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
    

def display_data():
    '''
    function to display the data
    '''
    return UserInformation.show_user_information()
