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