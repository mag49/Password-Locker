import pyperclip

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
    def authenticate_credentials(cls, user_name, email, password):
        '''
        Method that checks if the username and password are correct
        '''
        for cred in cls.cred_list:
            if cred.uname == uname and cred.passwrd == passwrd:
                return cred
        return 0