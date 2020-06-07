import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {
    "Amenity": Amenity,
    "BaseModel": BaseModel,
    "City": City,
    "Place": Place,
    "Review": Review,
    "State": State,
    "User": User
}

class FileStorage:
    __file_path = 'file.json'
    __objects = {}

    def __init__(self):
        pass

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        jsonObject = {}
        for key in self.__objects:
            jsonObject[key] = self.__objects[key].to_dict()

        jsonText = json.dumps(jsonObject)

        with open(self.__file_path, "w") as f:
            f.write(jsonText)
        f.close()

    def reload(self):
        try:
            with open(self.__file_path, 'r') as f:
                jsonObject = json.load(f)

                for key in jsonObject:
                    self.__objects[key] = classes[jsonObject[key]["__class__"]](**jsonObject[key])
        except:
            pass