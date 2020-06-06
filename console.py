#!/usr/bin/python3

import cmd

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit will exit the program"""
        return True

    def do_EOF(self, arg):
        """Exits the console"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()