#!/usr/bin/python3
"""
Ce module active l'interface en ligne de commande Python
"""
import json
import cmd
import sys
from models.base_model import BaseModel
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.city import City
from models.engine.file_storage import FileStorage
import shlex


def ev(val):
    """convertit les arguments appropriés en entier ou en décimal"""
    for i in val:
        try:
            yield json.loads(i)
        except Exception:
            yield i


def check_arg(arg, mesg):
    try:
        comd, nouveau_ID = arg.split('(')
    except Exception:
        print("** invalid command **")
        return None
    if comd != mesg:
        print("** invalid command **")
        return None
    return nouveau_ID.replace(')', '')


class HBNBCommand(cmd.Cmd):
    """Interface en ligne de commande pour le clone AirBnB"""
    prompt = '(hbnb) '
    file = None
    __classes = {'BaseModel': BaseModel, 'User': User, 'City': City,
                 'Place': Place, 'Amenity': Amenity, 'Review': Review,
                 'State': State}

    def do_EOF(self, line):
        """EOF(Ctrl + D)"""
        print("")
        return True

    def do_quit(self, argument_0):
        """Commande Quitter pour quitter le programme"""
        quit()

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass

    def do_create(self, args):
        """Crée une nouvelle instance d'une classe"""
        arg = shlex.split(args)
        if len(arg) < 1:
            print("** class name missing **")
            return
        if arg[0] not in self.__classes:
            print("** class doesn't exist **")
            return
        model = eval(arg[0])()
        model.save()
        print(model.id)

    def do_show(self, args):
        """Affiche la représentation en chaîne d'une instance"""
        arg = shlex.split(args)
        if len(arg) < 1:
            print("** class name missing **")
            return
        if arg[0] not in self.__classes:
            print("** class doesn't exist **")
            return
        if len(arg) < 2:
            print("** instance id missing **")
            return
        storage = FileStorage()
        storage.reload()
        tempD = storage.all()
        cls = "{}.{}".format(arg[0], arg[1])
        if cls in tempD.keys():
            obj = tempD.get(cls)
            print(obj)
        else:
            print("** no instance found **")

    def do_destroy(self, args):
        """Supprime une instance en fonction
        du nom de la classe et de l'identifiant"""
        arg = shlex.split(args)
        if len(arg) < 1:
            print("** class name missing **")
            return
        if arg[0] not in self.__classes:
            print("** class doesn't exist **")
            return
        if len(arg) < 2:
            print("** instance id missing **")
            return
        storage = FileStorage()
        storage.reload()
        tempD = storage.all()
        cls = "{}.{}".format(arg[0], arg[1])
        if cls in tempD.keys():
            del tempD[cls]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, args):
        """Crée une nouvelle instance d'une classe"""
        arg = shlex.split(args)
        if len(arg) >= 1 and arg[0] not in self.__classes:
            print("** class doesn't exist **")
            return
        storage = FileStorage()
        storage.reload()
        tempD = storage.all()
        Lists = []

        for key, obj in tempD.items():
            if len(arg) >= 1:
                if args[0] in key:
                    Lists.append(str(obj))
            else:
                Lists.append(str(obj))
        print(Lists)

    def do_update(self, args):
        """Met à jour une instance en fonction du nom de la classe et de
        l'identifiant en ajoutant ou en mettant à jour l'attribut"""
        arg = shlex.split(args)
        if len(arg) < 1:
            print("** class name missing **")
            return
        if arg[0] not in self.__classes:
            print("** class doesn't exist **")
            return
        if len(arg) < 2:
            print("** instance id missing **")
            return
        storage = FileStorage()
        storage.reload()
        tempD = storage.all()
        cls = "{}.{}".format(arg[0], arg[1])
        if cls not in tempD.keys():
            print("** no instance found **")
            return
        if len(arg) < 3:
            print("** attribute name missing **")
            return
        if len(arg) < 4:
            print("** value missing **")
            return
        arg = list(ev(arg))
        obj = tempD.get(cls)
        dict2 = obj.to_dict()
        dict2.update({arg[2]: arg[3]})
        obj2 = eval(arg[0])(**dict2)
        obj2.save()
        tempD.update({cls: obj2})
        storage.save()

    def default(self, args):
        """Gère les autres commandes"""
        args = shlex.split(args)
        try:
            arg1, arg = args[0].split('.')
            if len(args) > 1:
                for i in range(1, len(args)):
                    arg += args[i]
        except Exception:
            print("** invalid command **")
            return
        if arg1 not in self.classes:
            print("** class doesn't exist ")
            return
        storage = FileStorage()
        storage.reload()
        tempD = storage.all()
        new_list = []
        for key, value in tempD.items():
            if arg1 in key:
                new_list.append(str(value))

        if arg == "all()":
            print(new_list)

        elif arg == "count()":
            print(len(new_list))

        elif "show" in arg:
            nouveau_ID = check_arg(arg, "show")
            if not nouveau_ID:
                return
            for items in new_list:
                if nouveau_ID in items:
                    print(items)
                    return
            print("** no instance found **")

        elif "destroy" in arg:
            nouveau_ID = check_arg(arg, "destroy")
            if not nouveau_ID:
                return
            cls = f"{arg1}.{nouveau_ID}"
            if cls in tempD.keys():
                del tempD[cls]
                storage.save()
            else:
                print("** no instance found **")

        elif "update" in arg:
            new_arg = check_arg(arg, "update")
            if not new_arg:
                return
            if '{' in new_arg:
                try:
                    new_list = list(new_arg.split('{'))
                except Exception:
                    print("** invalid arguments **")
                    return
                nouveau_ID = new_list[0].replace(',', '')
                new_dict = new_list[1].replace('}', '')
                new_list = list(new_dict.split(','))
                cls = f"{arg1}.{nouveau_ID}"

                if cls in tempD.keys():
                    for item in new_list:
                        try:
                            valx = list(item.split(':'))
                            valx = list(ev(valx))
                        except Exception:
                            print("** attribute name missing **")
                            return
                        setattr(tempD[cls], valx[0], valx[1])
                    tempD[cls].save()
                    storage.save()

                else:
                    print("** no instance found **")

            elif len(args) == 3:
                nouveau_ID, new_key, new_value = new_arg.split(',')
                new_list = []
                new_list.append(new_value)
                new_list = list(ev(new_list))
                new_value = new_list[0]
                cls = f"{arg1}.{nouveau_ID}"
                if cls in tempD.keys():
                    setattr(tempD[cls], new_key, new_value)
                    storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** attribute missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
