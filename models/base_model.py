from uuid import uuid4
from datetime import datetime

class BaseModel:
    def __init__(self, *args, **kwargs):
        if len(kwargs) is not 0:
            for key, value in kwargs.items():
                if key is not "__class__":
                    if key is "created_at" or key is "updated_at":
                        self.__dict__[key] = datetime(value, "%Y-%m-%dT%H:%M:%S%z")
                    else:
                        self.__dict__[key] = value
        else:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.today()

    def __str__(self):
        className = self.__class__.__name__
        return "[{}] ({}) {}".format(className, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.today()

    def to_dict(self):
        dictCopy = self.__dict__.copy()
        dictCopy["created_at"] = self.created_at.isoformat()
        dictCopy["updated_at"] = self.updated_at.isoformat()
        dictCopy["__class__"] = self.__class__.__name__

        return dictCopy