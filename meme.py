"""Command-line tool to create memes using quotes and images."""

import os
import random
import argparse

from QuoteEngine import QuoteModel
from QuoteEngine import Ingestor
from MemeEngine import MemeCreator

def build_meme(path=None, body=None, author=None):
    """
    Create a meme by combining a quote and an image.

    Parameters:
    - path (str): path to the image file
    - body (str): quote body
    - author (str): quote author

    Returns:
    - str: path to the generated meme image
    """
    # Load image
    if path:
        image = path
    else:
        images = "./_data/photos/dog"
        imgs = [
            os.path.join(root, file)
            for root, _, files in os.walk(images)
            for file in files if file.endswith(('.jpg', '.png'))
        ]
        image = random.choice(imgs)

    # Load quote
    if body and author:
        quote = QuoteModel(body, author)
    elif body and not author:
        raise ValueError("Author is required if quote text is provided.")
    else:
        quote_file = [
            "./_data/DogQuotes/DogQuotesTXT.txt",
            "./_data/DogQuotes/DogQuotesDOCX.docx",
            "./_data/DogQuotes/DogQuotesPDF.pdf",
            "./_data/DogQuotes/DogQuotesCSV.csv"
        ]
        quotes = []
        for f in quote_file:
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)

    meme_generator = MemeCreator("./tmp")
    meme_path = meme_generator.create(image, quote.body, quote.author)

    return meme_path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Meme Generator CLI")
    parser.add_argument('--body', type=str,
                        help="Quote text to add to the meme")
    parser.add_argument('--author', type=str, help="Author of the quote")
    parser.add_argument('--path', type=str,
                        help="Path to the background image")

    args = parser.parse_args()

    try:
        result = build_meme(args.path, args.body, args.author)
        print(f"Meme successfully created at: {result}")
    except Exception as e:
        print(f"Error: {e}")
