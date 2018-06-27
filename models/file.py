"""Model for the file object"""
import os

from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from stat import S_ISDIR


from models.base import Base, Session

session = Session()

class File(Base):
    """Model that represents a file in the filesystem

    """
    __tablename__ = 'files'

    id = Column(Integer, primary_key=True, autoincrement=True)
    path = Column(String, unique=True)
    directory = Column(Boolean, default=False)
    last_modification = Column(DateTime)
    delete_date = Column(DateTime, nullable=True)

    def __str__(self):
        file_type = "Directory" if self.directory else "File"
        return f"{file_type}: {self.path} modified at {self.last_modification}"

    def __init__(self, path, directory, last_modification):
        self.path = path
        self.directory = directory
        self.last_modification = last_modification

    @classmethod
    def create(cls, filepath):
        """Returns an initialized instance of the class File based on the file path

        :param filepath:
        """
        file_info = os.stat(filepath)
        directory = S_ISDIR(file_info.st_mode)
        last_modification = file_info.st_mtime
        return cls(filepath, directory, last_modification)

    @classmethod
    def get_or_create(cls, filepath):
        return session.query(cls).filter(cls.path == filepath).first() or cls.create(filepath)

    def update_file_tree(self):
        pass

    def get_tree_changes(self, timestamp):
        pass
    # def create_children(self):
    #     if not directory:
    #         return []

    #     # Aquí el plan es que bajes un lvl y crees todos los hijos
