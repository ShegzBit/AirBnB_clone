#!/usr/bin/python3
"""
Basic console for HBNB  frontend usage
"""
import cmd
import cmd
import models.user
import models.state
import models.city
import models.place
import models.amenity
import models.review
import sys
import json
from ast import literal_eval
import re
import shlex

BaseModel = models.user.BaseModel
storage = models.storage
User = models.user.User
State = models.state.State
City = models.city.City
Place = models.place.Place
Amenity = models.amenity.Amenity
Review = models.review.Review


class HBNBCommand(cmd.Cmd):
    """
    Basic HBNB command interpreter
    """

    prompt = "(hbnb) "

    @staticmethod
    def to_numeral(obj):
        # checks if a string is convertible to a float
        try:
            int(obj)
            return int(obj)
        except ValueError:
            try:
                float(obj)
                return float(obj)
            except ValueError:
                return obj

    def do_quit(self, line):
        """Quit command to exit the program"""
        exit(0)

    def emptyline(self):
        """Handles empty line passed as command"""
        pass

    def do_EOF(self, line):
        """cleanly exits command line interface\
on EOF signal (on `ctrl + D`)"""
        print()
        exit(0)

    def do_create(self, line=""):
        """creates a new object and saves it to the file"""
        if line == "":
            print("** class name missing **")
            return
        classes = ({"Amenity": Amenity, "BaseModel": BaseModel, "User": User,
                    "City": City, "Place": Place,
                    "Review": Review, "State": State})

        if line not in classes:
            print("** class doesn't exist **")
            return
        NewModel = classes.get(line)
        obj = NewModel()
        print(obj.id)
        obj.save()

    def do_show(self, line=""):
        """Print the object of the class and id passed"""
        args = line.split()
        # line = "BaseModel id"
        # args = ["BaseModel", "<id>"]
        if line == "":
            print("** class name missing **")
            return
        classes = ({"Amenity": Amenity, "BaseModel": BaseModel, "User": User,
                    "City": City, "Place": Place,
                    "Review": Review, "State": State})

        if args[0] not in classes:
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
            if y.id == args[1] and y.__class__.__name__ == args[0]:
                print(y)
                id_exists = True
        if id_exists is False:
            print("** no instance found **")

    def do_destroy(self, line=""):
        """Destroy the object of the class and id passed"""
        args = line.split()
        if line == "":
            print("** class name missing **")
            return
        classes = ({"Amenity": Amenity, "BaseModel": BaseModel, "User": User,
                    "City": City, "Place": Place,
                    "Review": Review, "State": State})

        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        objects = storage._FileStorage__objects
        id_exists = False
        for x, y in objects.items():
            # If a dictionary has id = args[1] delete it
            if y.id == args[1] and y.__class__.__name__ == args[0]:
                del storage._FileStorage__objects[x]
                id_exists = True
                break
        if id_exists is False:
            print("** no instance found **")

    def do_all(self, line=""):
        """Prints all obj of type passed to all"""
        objects = storage._FileStorage__objects
        all = []
        # if line is empty string fetch all
        classes = ({"Amenity": Amenity, "BaseModel": BaseModel, "User": User,
                    "City": City, "Place": Place,
                    "Review": Review, "State": State})

        if line not in classes.keys() and line != '':
            print("** class doesn't exist **")
            return

        if line == "":
            all = [str(obj) for obj in objects.values()]
            line_empty = True
        # else fetch only ones with line the same as their class
        else:
            all = ([str(obj) for obj in objects.values()
                    if obj.__class__.__name__ == line])
        print(all)

    def do_update(self, line=""):
        """updates the attribute of a class"""
        attr = []
        if line == "":
            print("** class name missing **")
            return
        # list of available classes
        objects = storage._FileStorage__objects
        # local_classes = ["BaseModel", "User"]
        args = shlex.split(line)
        # line = 'User 121212 name "Hamida"'
        # args = ["User", "121212", "name", "Hamida"]
        # check for Class in available classes
        classes = ({"Amenity": Amenity, "BaseModel": BaseModel, "User": User,
                    "City": City, "Place": Place,
                    "Review": Review, "State": State})

        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        # get element from __objects and store in main_object
        main_object = None
        for obj in objects.values():
            class_name = obj.__class__.__name__
            obj_id = str(obj.id)
            if class_name == args[0] and obj_id == args[1]:
                main_object = obj
                break
        if main_object is None:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        # get all attrbutes from args
        # to give space for multiple assignment in the future
        attr = args[2:]
        if len(attr) % 2 != 0:
            attr = attr[:-1]
        # set first and second attribute
        # convert attribute to the right type first
        attr_1 = HBNBCommand.to_numeral(attr[1])
        setattr(main_object, attr[0], attr_1)
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
