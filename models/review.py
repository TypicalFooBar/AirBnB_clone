""" Documentation """

from models.base_model import BaseModel

class Review(BaseModel):
    """ Documentation """
    place_id = ''
    user_id = ''
    text = ''

    def __init__(self, *args, **kwargs):
        """ Construct new object """
        super().__init__(*args, **kwargs)