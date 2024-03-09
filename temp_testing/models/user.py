#!/usr/bin/python3
""" This script contains a module that includes
    a class that handles Users
"""

from models.base_model import BaseModel


class User(BaseModel):
    """Class to handle User """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
