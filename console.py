#!/usr/bin/python3

"""Importing neccessary modules"""

import cmd
import sys
import models
from models.base_model import BaseModel
from models import storage


classes = {"BaseModel": BaseModel}


class HBNBCommand(cmd.Cmd):
    """
    The HBNB command terminal
    ==========================

    The class used to create an use all HBNB associated commands
    """

    prompt = '(hbnb) '

    def do_create(self, model_type="None"):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id.
        Ex: $ create BaseModel
        """
        if model_type == "" or None:
            print("** class name missing **")
        elif model_type not in ["BaseModel", "City", "State",
                                "User", "Review", "Place", "Amenity"]:
            print("** class doesn't exist **")
        else:
            if model_type == "BaseModel":
                new_model = BaseModel()
            elif model_type == "State":
                new_model = State()
            elif model_type == "City":
                new_model = City()
            elif model_type == "User":
                new_model = User()
            elif model_type == "Place":
                new_model = Place()
            elif model_type == "Amenity":
                new_model = Amenity()
            elif model_type == "Review":
                new_model = Review()
            print(new_model.id)
            storage.new(new_model)
            storage.save()

    def do_show(self):
        """Print the string repersentation of an instance based on the class name and id"""
        pass

    def do_destroy(self):
        """Deletes an instance based on the class name and id (save the changes into the JSON file)"""
        pass

    def do_all(self):
        """Prints all string repersentation of all instances based or not on the class name"""
        pass

    def do_update(self):
        """Updates an instance based on class name and id by adding or updating arrtibute (Save changes to JSON file)"""
        pass
    
    def do_quit(self, line):
        """Quit command to exit the program"""
        return True 

    def do_EOF(self, line):
        """Providing a clean way to exit the interprater"""
        return True  # use CTRL+D to exit the interprater


if __name__ == '__main__':
    HBNBCommand().cmdloop()
