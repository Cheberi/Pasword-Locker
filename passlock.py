import string
import pyperclip
import random




class User:
    """
    Class that generates new instance of a user
    """
    user_list = []

    def __init__(self, username, password):
        self.username = username
        self.password = password


    def setUp(self):
        """
        Set up method to run before each test cases
        """
        self.new_user = User("Meshack Cheberi", "Meshack011")

    def save_user(self):
        """
        saves a new user to user list
        """

        User.user_list.append(self)

    @classmethod
    def get_user(cls):
        return cls.user_list

    def delete_user(self):
        """
        delete a saved account from the user list
        """
        User.user_list.remove(self)


class Credentials():
    """
    Create credential class to create new objects of credentials
    """
    credentials_list = []
    @classmethod
    def create_credentials(cls,username,password):
        """
        A method to confirm that a user exixts on the user_list or not
        """
        v_user = ""
        for user in User.user_list:
            if(user.username == username and user.password == password):
                v_user == user.username
        return v_user

    def __init__(self,account,username,password):
        """
        method that defines user credentials to be stored
        """

        self.account = account
        self.username = username
        self.password = password

    def save_details(self):

       """
       method to store new credentials in the credentials list
       """ 
       Credentials.credentials_list.append(self)

    def delete_credentials(self):
        """
        method that deletes an account's credentials for a certain account
        """
        Credentials.credentials_list.remove(self)

    @classmethod
    def find_credential(cls, account):
        """
        Method that take in account name and return credentials that matches the account name.
        """
        for credential in cls.credentials_list:
            if credential.account == account:
                return credential
    @classmethod
    def copy_password(cls, account):
        found_credentials = Credentials.find_credentials(account)
        pyperclip.copy(found_credentials.password)

    @classmethod
    def if_credential_exists(cls, account):
        """
        Method that checks if a credential exist and returns true or false.
        """
        for credential in cls.credentials_list:
            if credential.account == account:
                return True
        return False

    @classmethod
    def display_credentials(cls):
        """
        Method that returns all credentials in credential list
        """
        return cls.credentials_list

    def genPassword(stringLength=8):
         """
         Generate a random password string of letters and digits and special characters
         """
         password = string.ascii_uppercase + string.ascii_lowercase + string.digits + "~!@#$%^&*"
         return ''.join(random.choice(password) for i in range(stringLength))
