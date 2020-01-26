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