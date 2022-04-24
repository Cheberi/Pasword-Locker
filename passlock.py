class User:
    """
    Class that generates new instance of a user
    """
    user_list = []

    def __init__(self, username, password):
        self.username = username
        self.password = password
