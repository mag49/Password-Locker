from password import  Credential
from password import UserData
# import pyperclip
import unittest


class Testcredential(unittest.TestCase):
    '''
    '''


    def setUp(self):
        '''
        set up structure before every test
        '''
        self.new_credentials = Credential("maggiebae","you@email.com","pass")


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


class TestUserData(unittest.TestCase):
    '''
    '''


    def setUp(self):
        '''
        set up structure before every test
        '''
        self.new_user_data = UserData("facebook","maggiebae","you@email.com","pass")


    def tearDown(self):
        '''
        clean up after running each test
        '''
        UserData.user_data_list = []

    def test_init(self):
        '''
        Test for test case initialization"
        '''
        self.assertEqual(self.new_user_data.account_name, "facebook")
        self.assertEqual(self.new_user_data.account_username, "maggiebae")
        self.assertEqual(self.new_user_data.account_password, "pass")
    
    def test_add_password(self):
        '''
        Testing if the new website and password can be saved
        '''
        self.new_user_data.create_password()
        self.assertEqual(len(UserData.user_data_list),1)


    # def test_show_data(self):
    #     '''
    #     Testing if the data can be displayed.
    #     '''
    #     self.new_user_data.create_password()
    #     test_this = UserData("instagram","maggiebae","you@email.com", "pass")
    #     test_this.create_password()

    #     found_user_data = UserData.show_user_data("instagram")
    #     self.assertEqual(found_user_data.account_username,test_this.account_name)


if __name__ == "__main__":
    unittest.main()





