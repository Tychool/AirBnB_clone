#!/usr/bin/python3
""" This script contains a module that includes a class
    that handles Reviews
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Class that handles"""
    place_id = ""
    user_id = ""
    text = ""
