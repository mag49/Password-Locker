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