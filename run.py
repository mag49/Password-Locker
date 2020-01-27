#!/usr/bin/env python3
from password import Credential
from password import userInfomation
import random
import string
import time
import pyperclip

def create_credentials(user_name, password):
    '''
    function that creates new credentials
    '''
    new_credential = Credential(user_name,password)
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


def authenticate_credentials(user_name, password):
    '''
    '''
    return Credential.authenticate_credentials(user_name,password)