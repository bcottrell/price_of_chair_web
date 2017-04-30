from passlib.hash import pbkdf2_sha512 #the redline is trying to say that the package doesn't exist. Ignore this, it does exist.

class Utils(object):

    @staticmethod
    def hash_password(password):
        """
        Hashes password using pbkdf2_sha512
        :param password: The sha512 password from the Login/register form
        :return: A sha512 --> pbkdf2_sha512 encrypted password
        """
        return pbkdf2_sha512.encrypt(password)

    @staticmethod
    def check_hashed_password(password, hashed_password):
        """
        Checks that the password the user sent matches that of the database.
        The database password is encrypted more than the user's password at this stage
        :param password: sha512-hashed password
        :param hashed_password: pbkdf2_sha512 encrypted password (pbkdf2 is password secured in the database, more secure, but slow)
        :return: True if password match, false otherwise
        """
        return pbkdf2_sha512.verify(password, hashed_password)

