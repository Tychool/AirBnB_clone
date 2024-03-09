#!/usr/bin/python3
"""This script contains a module for HBNB command interpreter
for the HBNB project - Airbnb cloning
"""
import cmd
import json
import re
import models
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class for the HBNB project.
    """

    prompt = "(hbnb) "

    def default(self, line):
        """Handles unrecognized commands."""
        self._pre_command(line)

    def _pre_command(self, line):
        """
        Parses the input line and executes corresponding methods.

        Args:
            line (str): The input line entered by the user.
        """

        match = re.search(r"^(\w*)\.(\w+)(?:\(([^)]*)\))$", line)
        if not match:
            return line

        class_name = match.group(1)
        method = match.group(2)
        args = match.group(3)

        match_uid_and_args = re.search('^"([^"]*)"(?:, (.*))?$', args)
        if match_uid_and_args:
            uid = match_uid_and_args.group(1)
            attr_or_dict_str = match_uid_and_args.group(2)
        else:
            uid = args
            attr_or_dict_str = False

        attr_str = ""
        if method == "update" and attr_or_dict_str:
            match_dict = re.search('^({.*})$', attr_or_dict_str)
            if match_dict:
                self.update_dict(class_name, uid, match_dict.group(1))
                return ""
            match_attr_and_value = re.search(
                '^(?:"([^"]*)")?(?:, (.*))?$', attr_or_dict_str)
            if match_attr_and_value:
                attr_str = (match_attr_and_value.group(1) or "") + " " + (match_attr_and_value.group(2) or "")

        command = method + " " + class_name + " " + uid + " " + attr_str
        self.one_command(command)
        return command

    def update_dict(self, class_name, uid, string_dict):
        """
        Updates an instance with a dictionary of attributes.

        Args:
            class_name (str): Name of the class of the instance.
            uid (str): Unique ID of the instance.
            string_dict (str): Dictionary of attributes in string format.
        """

        json_string = string_dict.replace("'", '"')
        dictionary = json.loads(json_string)

        if not class_name:
            print("** class name missing **")
        elif class_name not in storage.classes():
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(class_name, uid)
            if key not in storage.all():
                print("** no instance found **")
            else:
                class_attributes_dict = storage.attributes()[class_name]
                for class_attribute, value in dictionary.items():
                    if class_attribute in class_attributes_dict:
                        value = class_attributes_dict[class_attribute](value)
                    setattr(storage.all()[key], class_attribute, value)
                storage.all()[key].save()

    def do_EOF(self, line):
        """Handles End Of File character."""
        print()
        return True

    def do_quit(self, line):
        """Exits the program."""
        return True

    def empty_line(self):
        """Doesn't do anything on ENTER."""
        pass

    def do_create(self, line):
        """Creates an instance."""
        if not line:
            print("** class name missing **")
        elif line not in storage.classes():
            print("** class doesn't exist **")
        else:
            new_instance = storage.classes()[line]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
        """Prints the string representation of an instance."""
        if not line:
            print("** class name missing **")
        else:
            words = line.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(words) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(words[0], words[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id."""
        if not line:
            print("** class name missing **")
        else:
            words = line.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(words) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(words[0], words[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, line):
        """Prints all string representations of all instances."""
        if line:
            words = line.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                instances = [str(obj) for instance_key, obj in storage.all().items()
                             if type(obj).__name__ == words[0]]
                print(instances)
        else:
            all_instances = [str(obj) for instance_key, obj in storage.all().items()]
            print(all_instances)

    def do_count(self, line):
        """Counts the instances of a class."""
        words = line.split(' ')
        if not words[0]:
            print("** class name missing **")
        elif words[0] not in storage.classes():
            print("** class doesn't exist **")
        else:
            matches = [instance_key for instance_key in storage.all() if instance_key.startswith(words[0] + '.')]
            print(len(matches))

    def do_update(self, line):
        """Updates an instance by adding or updating attribute."""
        if not line:
            print("** class name missing **")
            return

        rex_cmd_pattern = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
        match = re.search(rex_cmd_pattern, line)
        class_name = match.group(1)
        uid = match.group(2)
        attribute = match.group(3)
        value = match.group(4)
        if not match:
            print("** class name missing **")
        elif class_name not in storage.classes():
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(class_name, uid)
            if key not in storage.all():
                print("** no instance found **")
            elif not attribute:
                print("** attribute name missing **")
            elif not value:
                print("** value missing **")
            else:
                cast = None
                if not re.search('^".*"$', value):
                    if '.' in value:
                        cast = float
                    else:
                        cast = int
                else:
                    value = value.replace('"', '')
                class_attributes_dict = storage.attributes()[class_name]
                if attribute in class_attributes_dict:
                    value = class_attributes_dict[attribute](value)
                elif cast:
                    try:
                        value = cast(value)
                    except ValueError:
                        pass
                setattr(storage.all()[key], attribute, value)
                storage.all()[key].save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()

