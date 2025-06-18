"""Module that declares abstract base class giving interface."""
from abc import ABC, abstractmethod
from typing import List
from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """
    Abstract base class for actual Ingestor classes for diffent types of files.

    Each child class retrieves data from files and returns the desired ones.
    """

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path) -> bool:
        """Check whether path(file) is applicable for each ingestor class."""
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Abstract method to parse all file type."""
        pass
