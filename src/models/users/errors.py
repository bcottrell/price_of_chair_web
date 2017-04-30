
#These classes used to raise exceptions and provide the message in the objects, so they can be showed to the user

class UserNotExistError(Exception):
    def __init__(self, message):
        self.message = message

class IncorrectPasswordError(Exception):
    def __init__(self, message):
        self.message = message
