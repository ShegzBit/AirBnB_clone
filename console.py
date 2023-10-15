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
        """checks if a string is convertible to a float"""
        try:
            int(obj)
            return int(obj)
        except ValueError:
            try:
                float(obj)
                return float(obj)
            except ValueError:
                return obj

    @staticmethod
    def to_dict(strn):
        """Converts literal to py objects in this case dicts"""
        try:
            return literal_eval(strn)
        except (ValueError, SyntaxError):
            return strn

    def do_quit(self, line):
        """Quit command to exit the program"""
        exit(0)

    def emptyline(self):
        """Handles empty line passed as command"""
        pass

    def do_EOF(self, line):
        """cleanly exits command line interface on EOF signal (on `ctrl + D`)
"""
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
                storage.save()
                return
        # if id not found
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

    # ---------------<class_name> handler methods--------------------

    def handle_all(self, class_name, sub_args=[]):
        """Handles <classname>.all()"""
        objects = storage._FileStorage__objects
        all = ([obj for obj in objects.values()
                if obj.__class__.__name__ == class_name])
        print(all)

    def handle_count(self, class_name, sub_args=[]):
        """Handles <classname>.count()"""
        objects = storage._FileStorage__objects
        all = ([obj for obj in objects.values()
                if obj.__class__.__name__ == class_name])
        print(len(all))

    def handle_show(self, class_name, sub_args=[]):
        """Handles <classname>.all"""
        objects = storage._FileStorage__objects
        # handle for no id passed
        id = sub_args[0]
        if id == '':
            print("** instance id missing **")
            return
        # loop through the objects to find instance
        for obj in objects.values():
            obj_class = obj.__class__.__name__
            if obj_class == class_name and id == str(obj.id):
                print(obj)
                return
        # issue instance not found error if function still runs
        print("** no instance found **")

    def handle_destroy(self, class_name, sub_args=[]):
        """Handles <classname>.show"""
        objects = storage.all()
        # handle for no id passed
        id = sub_args[0]
        if id == '':
            print("** instance id missing **")
            return
        # loop through the objects to find instance
        id = sub_args[0]
        for name, obj in objects.items():
            obj_class = obj.__class__.__name__
            if obj_class == class_name and id == str(obj.id):
                del objects[name]
                storage.save()
                return
        # issue instance not found error if function still runs
        print("** no instance found **")

    def handler_update(self, class_name, sub_args):
        """Handles Updare called by <class_name>.update"""
        def dict_update(self, attr_dict):
            """Updates an object using a dictionary of attributes"""
            to_num = HBNBCommand.to_numeral
            for attr, value in attr_dict.items():
                setattr(self, attr, to_num(value))
            storage.save()
        is_dict = True
        if len(sub_args) < 1:
            print("** instance id missing **")
            return
        if len(sub_args) == 1 and sub_args[0] == '':
            print("** instance id missing **")
            return
        id_exists = False
        id = sub_args[0]
        # objects = storage._FileStorage__objects
        objects = storage.all()
        for obj in objects.values():
            cls_name_obj = obj.__class__.__name__
            if str(obj.id) == id and cls_name_obj == class_name:
                main_obj = obj
                id_exists = True
                break
        if id_exists is False:
            print("** no instance found **")
            return
        if len(sub_args) < 2:
            print("** attribute name missing **")
            return
        to_dict = HBNBCommand.to_dict
        if len(sub_args) > 1 and not isinstance(to_dict(sub_args[1]), dict):
            if len(sub_args) < 3:
                print("** value missing **")
                return
            to_numeral = HBNBCommand.to_numeral
            attr_dict = {sub_args[1]: to_numeral(sub_args[2])}
            is_dict = False
        if is_dict is True:
            attr_dict = to_dict(sub_args[1])
        dict_update(main_obj, attr_dict)

    # ------------<class_name> handler-------------------------------

    def default(self, line=""):
        """Default"""
        # line = User.all()
        # line = User.show(<id>)
        if line == "":
            return
        args = line.split('.')

        if args[0] not in (["User", "BaseModel", "Amenity", "City",
                            "Place", "Review", "State"]):
            print(f'*** Unknown syntax: {args[0]}')
            return

        # args[0] = "User"
        # args[1] = "all()"
        # args[1] = "show(<id>)"
        if len(args) == 1 and args[0] == line:
            return

        method = args[1].split('(')
        # method[0] = "all"
        # method[1] = ")"
        # method[1] = "<id>)"
        # method[1] ="id, key, value)"
        if len(method) == 1 and method[0] == args[1]:
            return
        _args = method[1].split(')')[0]
        # id = "id, key, value"
        # split id at ','
        # split only once if it contains a dictionary
        is_dict = False
        if '{' in _args and '}' in _args:
            sub_args = _args.split(",", 1)
        # else split as many times
        else:
            sub_args = _args.split(",")
        # args = ["id", "key", "value"]
        # id = [0]
        # -----------Undetailed behaviour from alx----------
        # strip all extra ' and " from id
        # split at space before quotes
        for i in range(len(sub_args)):
            if sub_args[i] != '""' and sub_args[i] != "''":
                sub_args[i] = sub_args[i].strip(" ")
                sub_args[i] = sub_args[i].strip('"')
                sub_args[i] = sub_args[i].strip("'")
            if is_dict is True:
                break
        commands = ({"all": self.handle_all, "count": self.handle_count,
                    "show": self.handle_show, "destroy": self.handle_destroy,
                     "update": self.handler_update})
        for x, y in commands.items():
            if method[0] == x:
                y(args[0], sub_args)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
