#!/usr/bin/python3
import cmd
import json
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.review import Review
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place

"""
This module of console these commands."""

class HBNBCommand(cmd.Cmd):
    """Custom command interpreter for AirBnB project."""

    prompt = "(hbnb) "
    __classes = {'BaseModel': BaseModel, 'User': User, 'City': City,
               'Place': Place, 'Amenity': Amenity, 'Review': Review,
               'State': State}
    def do_quit(self, arg):
        """Exit the program."""
        return True
    
    def do_EOF(self, arg):
        """Exit the program on EOF."""
        print("")
        return True
    
    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass

    def do_create(self, arg):
        """Create a new class instance and print its id."""
        argcom = arg.split()

        if len(argcom) == 0:
            print("** class name missing **")
        elif argcom[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            new_cls = BaseModel()
            new_cls.save()
            print(new_cls.id)

    def do_show(self, arg):
        """Print the string representation of an instance."""
        argcom = arg.split()

        if len(argcom) == 0:
            print("** class name missing **")
        elif argcom[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argcom) < 2:
            print("** instance id missing **")
        else:
            obj_id = storage.all()
            cls = "{}.{}".format(argcom[0], argcom[1])
            if cls in obj_id:
                print(obj_id[cls])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Delete an instance based on class name and id."""
        argcom = arg.split()

        if len(argcom) == 0:
            print("** class name missing **")
        elif argcom[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argcom) < 2:
            print("** instance id missing **")
        else:
            obj_id = storage.all()
            cls = "{}.{}".format(argcom[0], argcom[1])
            if cls in obj_id:
                del obj_id[cls]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """ Print all instances in string representation """
        obj_id = storage.all()
        argcom = arg.split()

        if len(argcom) == 0:
            for cls, value in obj_id.items():
                print(str(value))
        elif argcom[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            for cls, value in obj_id.items():
                if cls.split('.')[0] == argcom[0]:
                    print(str(value))

    def do_update(self, arg):
        """Update an instance attribute based on class name and id."""
        argcom = arg.split()

        if len(argcom) == 0:
            print("** class name missing **")
            return
        if argcom[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(argcom) < 2:
            print("** instance id missing **")
            return
        cls = "{}.{}".format(argcom[0], argcom[1])
        if cls in storage.all():
            obj = storage.all()[cls]
            if len(argcom) < 4:
                print("** attribute name missing **")
                return
            setattr(obj, argcom[2], argcom[3].strip('"'))
            storage.save()
        else:
            print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()

