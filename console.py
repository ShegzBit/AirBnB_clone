#!/usr/bin/env python3
"""
Basic console for HBNB  frontend usage
"""
import cmd
import models.base_model

BaseModel = models.base_model.BaseModel
storage = models.storage



class HBNBCommand(cmd.Cmd):
    """
    Basic HBNB command interpreter
    """

    prompt = "(hbnb)"
    def preloop(self) -> None:
        self.classes = {"BaseModel": BaseModel}
        return super().preloop()
    def do_quit(self, line):
        """Quit command to exit the program
"""
        exit(0)
    
    def emptyline(self):
        """Handles empty line passed as command
"""
        pass

    def do_EOF(self, line):
        """cleanly exits command line interface on EOF signal (on `ctrl + D`)
"""
        exit(0)
    
    def do_create(self, line=""):
        """creates a new object and saves it to the file
"""
        if line == "":
            print("** class name missing **")
            return
        if line not in self.classes:
            print("** class doesn't exist **")
            return
        model = self.classes.get(line)
        obj = model()
        print(obj.id)
        obj.save()
    
    def do_show(self, line=""):
        """Print the object of the class and id passed
"""
        args = line.split()
        if line == "":
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        objects = storage._FileStorage__objects
        id_exists = False
        for x, y in objects.items():
            # If a dictionary has id = args[1]: Create new object instance
            # and print
            if y.id == args[1]:
                model = self.classes.get(args[0])
                print(y)
                id_exists = True
        if id_exists is False:
            print("** no instance found **")
        
    def do_destroy(self, line=""):
        """Destroy the object of the class and id passed
"""
        args = line.split()
        if line == "":
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        objects = storage._FileStorage__objects
        id_exists = False
        for x, y in objects.items():
            # If a dictionary has id = args[1] delete it
            if y.id == args[1]:
                del storage._FileStorage__objects[x]
                id_exists = True
                break
        if id_exists is False:
            print("** no instance found **")
        

if __name__ == '__main__':
    HBNBCommand().cmdloop()