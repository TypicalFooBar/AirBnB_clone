""" Documentation """

from models.base_model import BaseModel

class User(BaseModel):
    """ Documentation """
    email = ''
    password = ''
    first_name = ''
    last_name = ''

    def __init__(self, *args, **kwargs):
        """ Construct new user """
        super().__init__(*args, **kwargs)