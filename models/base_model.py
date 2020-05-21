from uuid import uuid4
from datetime import datetime

class BaseModel:
    def __init__(self):
        self.id = str(uuid4())
        self.created_at = self.update_at = datetime.today()

    def __str__(self):
        className = self.__class__.__name__
        return "[{}] ({}) {}".format(className, self.id, self.__dict__)

    def save(self):
        self.update_at = datetime.today()

    def to_dict(self):
        dictCopy = self.__dict__.copy()
        dictCopy["__class__"] = self.__class__.__name__

        return dictCopy