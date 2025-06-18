"""Module that Encapsulate ingestors for differnt types of files."""

from QuoteEngine.QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface
from .CSVImporter import CSVImporter
from .DocxImporter import DocxImporter
from .PDFImporter import PDFImporter
from .TextImporter import TextImporter
from typing import List


class Ingestor(IngestorInterface):
    """Class encapsulating each impoter modules."""

    ingestors = [CSVImporter, DocxImporter, PDFImporter, TextImporter]

    @classmethod
    def parse(cls, path) -> List[QuoteModel]:
        """Pasre paths(files) by appropriate ingestor."""
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
