#!/usr/bin/python3
"""Thsis script contains a Module for Class: FileStorage"""
import json
import os
import datetime


class FileStorage:
    """File storage class"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the  __objects dict."""
        return FileStorage.__objects

    def new(self, obj):
        """Initialize <obj class name>.id in the dict:  __objects"""

        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serialization of Dict: __objects to the JSON file (path: __file_path)"""

        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(d, f)

    def classes(self):
        """Dict: Valid classes and their references"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        class_init = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review}
        return class_init

    def reload(self):
        """Refresh and reload objects from storage"""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as file_in:
            object_dict = json.load(file_in)
            object_dict = {class_instance: self.class_init()[value["__class__"]](**value)
                        for class_instance, value in object_dict.items()}
            # TODO: overwrite or insert?
            FileStorage.__objects = object_dict

    def attributes(self):
        """Atributes and class names"""
        instance_attributes = {
            "BaseModel":
                     {"id": str,
                      "created_at": datetime.datetime,
                      "updated_at": datetime.datetime},
            "User":
                     {"email": str,
                      "password": str,
                      "first_name": str,
                      "last_name": str},
            "State":
                     {"name": str},
            "City":
                     {"state_id": str,
                      "name": str},
            "Amenity":
                     {"name": str},
            "Place":
                     {"city_id": str,
                      "user_id": str,
                      "name": str,
                      "description": str,
                      "number_rooms": int,
                      "number_bathrooms": int,
                      "max_guest": int,
                      "price_by_night": int,
                      "latitude": float,
                      "longitude": float,
                      "amenity_ids": list},
            "Review":
            	    {"place_id": str,
                     "user_id": str,
                     "text": str}
        }
        return instance_attributes

