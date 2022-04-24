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

       