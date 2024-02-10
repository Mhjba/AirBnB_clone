#!/usr/bin/python3
"""Creates a single FileStorage instance for your application."""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
