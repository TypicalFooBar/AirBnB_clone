from uuid import uuid4
from datetime import datetime
import models

class BaseModel:
    def __init__(self, *args, **kwargs):
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        self.__dict__[key] = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    else:
                        self.__dict__[key] = value
        else:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        className = self.__class__.__name__
        return "[{}] ({}) {}".format(className, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        dictCopy = self.__dict__.copy()
        dictCopy["created_at"] = self.created_at.isoformat()
        dictCopy["updated_at"] = self.updated_at.isoformat()
        dictCopy["__class__"] = self.__class__.__name__

        return dictCopy