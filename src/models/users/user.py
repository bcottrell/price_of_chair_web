import uuid
from src.common.database import Database
from src.common.utils import Utils
import src.models.users.errors as UserErrors

class User(object):
    def __init__(self, email, password, _id=None):
        self.email = email
        self.password = password
        #create unique user identifiers if it doesn't exist. use hex version b/c mongodb doesn't support storing the object type
        self._id = uuid.uuid4().hex if _id is None else _id

    # __repr__ is used to construct what the output looks like
    def __repr__(self):
        return "<User {}>".format(self.email)

    #using static b/c we aren't talking about an specific user object, we are checking to see email and password is valid, then create the user object
    @staticmethod
    def is_login_valid(email, password):
        """
        This method verifies that an email/password combo (as sent by the site forms) is valid or not.
        Checks that the email exists, and that the password associated to that email is correct.
        :param email: The user's email
        :param password: A sha512 hashed password
        :return: True if valid, False otherwise
        """
        user_data = Database.find_one("users", {"email": email}) # password in sha512 --> pbkdf2_sha512
        if user_data is None:
            #Tell the user that their email doesn't exist
            raise UserErrors.UserNotExistError("Your user doesn't exist.")
        if not Utils.check_hashed_password(password, user_data['password']):
            #Tell the user that their password is wrong
            raise UserErrors.IncorrectPasswordError("Your password was wrong")

        return True