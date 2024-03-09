#!/usr/bin/python3
"""This script contains an inheritance class: BaseModel
For all classes"""

import uuid
from uuid import uuid4
from models import storage
from datetime import datetime


class BaseModel:
    """inheritance class for all classes"""

    def __init__(self, *args, **kwargs):
        """Initialize instance

        Args:
            - *args: Arguments
            - **kwargs: Key values
        """

        if kwargs:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Official string representation"""

        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Update and serialize updated_at"""

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Dictionary of keys in __dict__"""

        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict

