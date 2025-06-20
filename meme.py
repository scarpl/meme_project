"""Command-line tool to create memes using quotes and images."""

import os
import random
import argparse
from QuoteEngine import QuoteModel
from QuoteEngine import Ingestor
from MemeEngine import MemeEngine


def build_meme(image_path=None, quote_text=None, quote_author=None):
    """
    Create a meme by combining a quote and an image.

    Parameters:
    - image_path (str): path to the image file
    - quote_text (str): quote body
    - quote_author (str): quote author

    Returns:
    - str: path to the generated meme image
    """
    # Load image
    if image_path:
        image = image_path
    else:
        image_dir = "./_data/photos"
        image_files = [
            os.path.join(root, file)
            for root, _, files in os.walk(image_dir)
            for file in files if file.endswith(('.jpg', '.png'))
        ]
        image = random.choice(image_files)

    # Load quote
    if quote_text and quote_author:
        quote = QuoteModel(quote_text, quote_author)
    elif quote_text and not quote_author:
        raise ValueError("Author is required if quote text is provided.")
    else:
        quote_sources = [
            "./_data/DogQuotes/DogQuotesTXT.txt",
            "./_data/DogQuotes/DogQuotesDOCX.docx",
            "./_data/DogQuotes/DogQuotesPDF.pdf",
            "./_data/DogQuotes/DogQuotesCSV.csv"
        ]
        all_quotes = []
        for file in quote_sources:
            all_quotes.extend(QuoteLoader.load(file))

        quote = random.choice(all_quotes)

    meme_generator = MemeCreator("./tmp")
    meme_path = meme_generator.create(image, quote.body, quote.author)

    return meme_path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Meme Generator CLI")
    parser.add_argument('--body', type=str, help="Quote text to add to the meme")
    parser.add_argument('--author', type=str, help="Author of the quote")
    parser.add_argument('--path', type=str, help="Path to the background image")

    args = parser.parse_args()

    try:
        result = build_meme(args.path, args.body, args.author)
        print(f"Meme successfully created at: {result}")
    except Exception as e:
        print(f"Error: {e}")
