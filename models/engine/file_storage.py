#!/usr/bin/python3
"""This module contains a class for FileStorage management."""

import json
import os
import datetime

class FileStorage:
    """A class to manage file-based storage."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Get all objects stored in the file."""
        return FileStorage.__objects

    def new(self, obj):
        """Add a new object to the storage.

        Args:
            obj: The object to be added.
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Save objects to the file in JSON format."""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            serialized_objects = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(serialized_objects, f)

    def classes(self):
        """Get a dictionary of valid classes and their references."""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        class_init = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
        }
        return class_init

    def reload(self):
        """Reload objects from the file."""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as file_in:
            object_dict = json.load(file_in)
            object_dict = {
                class_instance: self.classes()[value["__class__"]](**value)
                for class_instance, value in object_dict.items()
            }
            FileStorage.__objects = object_dict

    def attributes(self):
        """Get a dictionary of class attributes and their data types."""
        instance_attributes = {
            "BaseModel": {
                "id": str,
                "created_at": datetime.datetime,
                "updated_at": datetime.datetime
            },
            "User": {
                "email": str,
                "password": str,
                "first_name": str,
                "last_name": str
            },
            "State": {"name": str},
            "City": {
                "state_id": str,
                "name": str
            },
            "Amenity": {"name": str},
            "Place": {
                "city_id": str,
                "user_id": str,
                "name": str,
                "description": str,
                "number_rooms": int,
                "number_bathrooms": int,
                "max_guest": int,
                "price_by_night": int,
                "latitude": float,
                "longitude": float,
                "amenity_ids": list
            },
            "Review": {
                "place_id": str,
                "user_id": str,
                "text": str
            }
        }
        return instance_attributes

