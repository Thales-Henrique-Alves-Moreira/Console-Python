from os.path import dirname
from os import listdir

folders = listdir(dirname(__file__))
folders.remove("__init__.py")
folders.remove("__pycache__")

__all__ = folders
