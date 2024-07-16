#! usr/bin/python3
from random import randint
import uuid

class User:
    """This class is created to make users that want to log in and take their information such as username
    , password, phone number and make automatically id for them :
    username must be unique and specific and password is private"""
    user_names = []

    def __init__(self, username: str = None, password: str = None, id: int = None, phone_number: int = None, birthday: str = None, time = None) -> None:
        """This method is made to take the values of username, password and phone number from the user and
        put it for the user.It also creates a unique ID for the user, but in this code,
        it is more for creating the user object itself.""" 
        self.phone_number = phone_number
        self._password = password
        self.time = time
        if password != None:
            if len(password) >= 4:
                self._password = password
            else:
                print("password must have more than 4 charactar....")

        
 
        user_id = uuid.uuid4()
        uuid_str = str(user_id)
        parsed_uuid = uuid.UUID(uuid_str)
        self.id = parsed_uuid
       
        self._birthday = birthday
    @property
    def username1(self) -> str:
        """getter for username"""
        return self._username

    @username1.setter
    def username1(self, value: int) -> None:
        """setter for username and validates to find out whether this username has already been selected or not"""
        if value not in User.user_names:
            self._username = value
            User.user_names.append(value)
        else:
            print("Warning: username already exist...")

    @property
    def phone_number1(self) -> int:
        """getter for phone number"""
        return self.phone_number

    @phone_number1.setter
    def phone_number1(self, phone_number: int) -> None:
        """setter for username"""
        self.phone_number = phone_number

    @property
    def password1(self) -> str:
        """getter for password"""
        return self._password

    @password1.setter
    def password1(self, password: str) -> None:
        """setter for password and make sure that the input password is more than 4 character"""
        if len(password) >= 4:
            self._password = password
        else:
            print("password must have more than 4 charactar....")

    
    def id(self) -> str:
        """getter for id"""
        return self.id
    
    @property
    def birthday1(self):
        """The birthday property."""
        return self._birthday

    @birthday1.setter
    def birthday1(self, value):
        """setter for birthday"""
        self._birthday = value
         
    
        
