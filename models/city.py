""" Documentation """

from models.base_model import BaseModel

class City(BaseModel):
    """ Documentation """
    state_id = ''
    name = ''

    def __init__(self, *args, **kwargs):
        """ Construct new object """
        super().__init__(*args, **kwargs)