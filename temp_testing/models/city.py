#!/usr/bin/python3
"""
This script contians a module that includes class
to handle Cities
"""

from models.base_model import BaseModel


class City(BaseModel):
    """Class to handle City"""

    state_id = ""
    name = ""
