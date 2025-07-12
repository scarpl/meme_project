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
    def parse(cls, file_path: str):
        """
        Extracts citations from file .docx file format

        Paragraphs must have format:
            "Citation Text" - Author
        """
        if not cls.can_ingest(file_path):
            raise Exception(f"Cannot process file: {file_path}")

        sentences = []

        try:
            document = docx.Document(file_path)
        except Exception as e:
            raise Exception(f"Failed to open file: {e}")

        for i in document.paragraphs:
            if i.text != "":
                parse = i.text.split('-')
                body = parse[0].strip().strip('"')
                author = parse[1].strip()
                sentences.append(QuoteModel(body, author))

        return sentences
