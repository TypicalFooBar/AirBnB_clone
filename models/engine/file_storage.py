import json

class FileStorage:
    __file_path = None
    __objects = {}

    def __init__(self):
        pass

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects["{}.{}".format(obj.__name__, obj.id)] = obj

    def save(self):
        jsonText = json.dumps(self.__objects)

        with open(self.__file_path, "w") as f:
            f.write(jsonText)
        f.close()

    def reload(self):
        try:
            with open(self.__file_path, 'r') as f:
                jsonObject = json.load(f)

                for key in jsonObject:
                    self.__objects[key] = jsonObject[key]
        except:
            pass