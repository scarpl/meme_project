
"""Module to parse data from file with extention .csv."""

from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
import pandas


class CSVImporter(IngestorInterface):
    """Module to read CSV file."""

    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str):
        """
        Load quotes from a .csv file.

        Expects columns: 'body' and 'author'.
        """
        if not cls.can_ingest(path):
            raise Exception(f"Cannot ingest file type: {path}")

        quotes = []

        df = pandas.read_csv(path, header=0)

        for i , row in df.iterrows():
            new_quote = QuoteModel(row['body'], row['author'])
            quotes.append(new_quote)

        return quotes
