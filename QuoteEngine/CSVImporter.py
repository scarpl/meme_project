
"""Module to parse data from file with extention .csv."""

from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
import pandas as pd
import sys


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
            raise Exception(f"Cannot ingest file: {path}")

        sentences = []

        try:
            df = pd.read_csv(path)
            for i, row in df.iterrows():
                new_quote = QuoteModel(row['body'], row['author'])
                sentences.append(new_quote)

        except Exception as e:
            raise IOError(f"Error reading CSV file: {e}")

        return sentences
