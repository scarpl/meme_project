"""
Abstract base class for actual Ingestor classes for diffent types of files.

Each child class retrieves data from files and returns the desired ones.
"""
from abc import ABC, abstractmethod
from typing import List
from .QuoteModel import QuoteModel


class IngestorInterface(ABC):

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path) -> bool:
        """
        Extracts the file extension from the file path
        and verify if it is applicable within the ingestor class.
        """
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse any type of file.
        """
        pass
