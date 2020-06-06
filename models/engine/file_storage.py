import json

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
                    self.__objects[key] = jsonObject[key]
        except:
            pass