from password import  Credential

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
        self.assertEqual(self.new_credentials.password, "pass")

    def test_authentication(self):
        '''
        Tests proper authentication for log in purposes
        '''
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credential.credential_list), 1)


    class TestUserInformation(unittest.TestCase):
        '''
        '''


    def setUp(self):
        '''
        set up structure before every test
        '''
        self.new_user_information = UserInformation("facebook","maggiebae","pass")


    def tearDown(self):
        '''
        clean up after running each test
        '''
        UserInformation.user_information_list = []

    def test_init(self):
        '''
        Test for test case initialization"
        '''
        self.assertEqual(self.new_user_information.account_name, "facebook")
        self.assertEqual(self.new_user_information.account_user_name, "maggiebae")
        self.assertEqual(self.new_user_information.account_password, "pass")
    
    def test_add_password(self):
        '''
        Testing if the new website and password can be saved
        '''
        self.new_user_information.create_password()
        self.assertEqual(len(UserInformation.user_information_list),1)


    def test_show_information(self):
        '''
        Testing if the data can be displayed.
        '''
        self.new_user_information.create_password()
        test_this = UserInformation("instagram","maggiebae", "pass")
        test_this.create_password()

        found_user_information = UserInformation.show_user_information("instagram")
        self.assertEqual(found_user_information.account_name,test_this.account_name)


if __name__ == "__main__":
    unittest.main()





