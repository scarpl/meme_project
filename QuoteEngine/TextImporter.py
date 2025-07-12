"""Import text file."""
from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TextImporter(IngestorInterface):
    """Helper class to read text file."""

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str):
        """
        Read a .txt file and return a list of QuoteModel instances.

        Each line must follow the format: "quote text" - author
        """
        if not cls.can_ingest(path):
            raise Exception(f"Cannot process file: {path}")

        sentences = []

        try:
            with open(path, 'r', encoding='utf-8') as file:
                for i in file:
                    if "-" in i:
                        parts = i.strip().split("-")
                        body = parts[0].strip().strip('"')
                        author = parts[1].strip()
                        sentences.append(QuoteModel(body, author))
        except Exception as e:
            raise Exception(f"Error reading TXT file: {e}")

        return sentences
