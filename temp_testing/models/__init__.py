#!/usr/bin/python3
"""
__init__ method - A models package, that initializes
package Module for FileStorage
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
