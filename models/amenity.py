""" Documentation """

from models.base_model import BaseModel

class Amenity(BaseModel):
    """ Documentation """
    name = ''

    def __init__(self, *args, **kwargs):
        """ Construct new object """
        super().__init__(*args, **kwargs)