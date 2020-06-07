#!/usr/bin/python3
""" Documentation """

import cmd
import shlex
import models
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

class HBNBCommand(cmd.Cmd):
    """ Documentation """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """ Quit will exit the program """
        return True

    def do_EOF(self, arg):
        """ Exits the console """
        return True

    def emptyline(self):
        """ Do nothing on an empty line """
        return False

    def do_create(self, arg):
        """ Creates a new object """
        args = shlex.split(arg)

        if len(args) == 0:
            print("** class name missing **")
            return False
        
        if args[0] in classes:
            newObject = classes[args[0]]()
        else:
            print("** class doesn't exist **")
            return False

        print(newObject.id)
        newObject.save()

    def do_show(self, arg):
        """ Prints the contents of an object specified by an ID """
        args = shlex.split(arg)

        if len(args) == 0:
            print("** class name missing **")
            return False

        if args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]

                if key in models.storage.all():
                    print(models.storage.all()[key])
                else:
                    print("** no instance found **")
            else:
                print ("** instance id missing **")
        else:
            print ("** class doesn't exist **")

    def do_destroy(self, arg):
        """ Removes an object referenced by ID """
        args = shlex.split(arg)

        if len(args) == 0:
            print("** class name missing **")
            return
        
        if args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]

                if key in models.storage.all():
                    models.storage.all().pop(key)
                    models.storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """ Prints all objects """
        args = shlex.split(arg)
        objects = []

        if len(args) == 0:
            for value in models.storage.all().values():
                objects.append(str(value))

            print("[" + ", ".join(objects) + "]")
        elif args[0] in classes:
            for key in models.storage.all():
                if args[0] in key:
                    objects.append(str(models.storage.all()[key]))

            print("[" + ", ".join(objects) + "]")
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """ Updates an object """
        args = shlex.split(arg)

        if len(args) < 1:
            print("** class name missing **")
            return
        elif args[0] not in classes:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return

        key = args[0] + "." + args[1]

        if key not in models.storage.all():
            print("** no instance found **")
            return
        elif len(args) < 3:
            print("** attribute name missing **")
            return
        elif len (args) < 4:
            print ("** value missing **")
            return

        setattr(models.storage.all()[key], args[2], args[3])
        models.storage.all()[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()