"""Module to parse data from file with extention .docx."""
from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
import docx


class DocxImporter(IngestorInterface):
    """
    Load quotes from a .docx file.

    Expects format: "quote text" - author
    """

    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str):
        """Parse Docx file and list of quote models."""
        if not cls.can_ingest(path):
            raise Exception(f"Cannot process file: {path}")

        quotes = []

        try:
            document = docx.Document(path)
        except Exception as e:
            raise Exception(f"Failed to open DOCX file: {e}")

        for para in document.paragraphs:
            if para.text != "":
                parse = para.text.split('-')
                body = parse[0].strip().strip('"')
                author = parse[1].strip()
                new_quote = QuoteModel(body, author)
                quotes.append(new_quote)

        return quotes
