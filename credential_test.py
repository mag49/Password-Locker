from password import  Credential
from password import UserInformation
import pyperclip
import unittest


class Testcredential(unittest.TestCase):
    '''
    '''


    def setUp(self):
        '''
        set up structure before every test
        '''
        self.new_credentials = Credential("maggiebae","pass")


    def tearDown(self):
        '''
        clean up after running each test
        '''
        Credential.credential_list = []

    def test_init(self):
        '''
        Test for case initialization
        '''
        self.assertEqual(self.new_credentials.user_name, "maggiebae")
        self.assertEqual(self.new_credentials.passwOrd, "pass")

    def test_authentication(self):
        '''
        Tests proper authentication for log in purposes
        '''
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credential.credential_list), 1)


