#!/usr/bin/python3

"""
This module defines a base class BaseModel for all classes to inherit from.
"""

import uuid
from uuid import uuid4
from datetime import datetime
from models import storage  # Assuming storage is imported from models

class BaseModel:
    """
    Base class for all classes to inherit from.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel class.

        Args:
            *args: Positional arguments.
            **kwargs: Keyword arguments.
        """

        if kwargs:
            # Iterate through keyword arguments
            for key, value in kwargs.items():
                # Convert created_at and updated_at strings to datetime objects
                if key == "created_at":
                    self.created_at = datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f"
                    )
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f"
                    )
                else:
                    # Set other attributes dynamically
                    setattr(self, key, value)
        else:
            # Generate a unique ID if no ID is provided
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        Returns the official string representation of the object.
        """

        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__
        )

    def save(self):
        """
        Updates and serializes the updated_at attribute.
        """

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary representation of the object.
        """

        object_dict = self.__dict__.copy()
        object_dict["__class__"] = type(self).__name__
        object_dict["created_at"] = object_dict["created_at"].isoformat()
        object_dict["updated_at"] = object_dict["updated_at"].isoformat()
        return object_dict

