#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    """that contains the entry point of the command interpreter:"""
    
    prompt = "(hbnb) "
    
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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
