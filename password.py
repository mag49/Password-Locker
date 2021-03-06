# import pyperclip

class Credential:

    """
    Class that generates new instances of credentials.
    """

    credential_list = [] # Empty credential list
    

    def __init__(self,user_name,email,password):

        self.user_name = user_name
        self.email= email
        self.password=password
        

         # Init method up here

    def save_credentials(self):

        '''
        save_credentials method saves credential objects into credential_list
        '''

        Credential.credential_list.append(self)


    def delete_credentials(self):

        '''
        delete_credentials method deletes a saved credential from the credential_list
        '''

        Credential.credential_list.remove(self)

    @classmethod
    def find_credential(cls,username):
        '''
        Method that finds if the username exist and returns true or false.

        Args:
            username: username to search for
        Returns :
            Boolean: True or false depending on whether it exist
        '''

        for credential in cls.credential_list:
            if credential.user_name == user_name:
                return True
        return False

    @classmethod
    def copy_email(cls,email):
        credential_found = Contact.find_by_email(email)
        pyperclip.copy(credential_found.email)    


    @classmethod
    def authenticate_credentials(cls, user_name, password):
        '''
        Method that checks if the username email and password are correct
        '''
        for credential in cls.credential_list:
            if credential.user_name == user_name and credential.password == password:
                return credential
        return 0

class UserData:
    '''
    class that generates new instance of users
    '''
    user_data_list = []
    user_data_list2 = str(user_data_list)

    def __init__(self, account_name,account_username, account_email, account_password):
        '''
        '''
        self.account_name = account_name
        self.account_username =  account_username
        self.account_email = account_email
        self.account_password = account_password

    def create_email(self):
        '''
        creates an email
        '''
        return UserData.user_data_list.append(self)

    def create_password(self):
        '''
        creates a password and account name
        '''
        return UserData.user_data_list.append(self)    

    # @classmethod
    # def show_user_data(cls):
    #     '''
    #     Displays all passwords and other acc0unt details 
    #     '''
    #     return cls.user_data_list 

    # @classmethod
    # def show_user_data(cls, account_name):
    #     '''
    #     Finds user information using the user account name
    #     '''

    #     for found in cls.user_data_list2:
    #         if found == account_name:
    #             return found

    @classmethod
    def data_exists(cls, account_name):
        '''
        Checks if user information exists
        '''
        for data in cls.user_data_list:
            if data.account_name == account_name:
                return data

    
