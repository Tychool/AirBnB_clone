#!/usr/bin/python3

"""
This script contains a base class BaseModel
for all classes to inherit from.
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
        Initializes instance.

        Args:
            - *args: Positional arguments
            - **kwargs: Keyword arguments
        """

        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at":
                    self.created_at = datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f"
                    )
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f"
                    )
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        Official string representation.
        """

        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__
        )

    def save(self):
        """
        Updates and serializes updated_at.
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

