"""Image meme builder module using Pillow."""

import os
import random
from PIL import Image, ImageDraw, ImageFont
from QuoteEngine import Ingestor, QuoteModel
import argparse


class MemeCreator:
    """Handles the generation of meme images."""

    def __init__(self, output_dir):
        """
        Initialize the meme creator.

        Parameters:
        - output_dir (str): Path where generated memes will be saved.
        """
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def create(self, path, quote_text, quote_author, max_width=500):
        """
        Create a meme with text and author on the given image.

        Parameters:
        - path (str): Path to the input image
        - quote_text (str): The quote body to display
        - quote_author (str): The quote author to display
        - max_width (int): Optional max width of the meme image

        Returns:
        - str: Path to the generated meme image
        """
        try:
            with Image.open(path) as img:
                original_ratio = img.height / img.width
                new_width = min(max_width, img.width)
                new_height = int(new_width * original_ratio)
                img = img.resize((new_width, new_height))

                draw = ImageDraw.Draw(img)

                font_path = "./_data/arial.ttf"
                font_size = int(new_height / 20)
                font = ImageFont.truetype(font_path, font_size)

                full_text = f'"{quote_text}"\n- {quote_author}'

                # Calculate random placement
                x = random.randint(10, new_width // 4)
                y = random.randint(10, new_height - int(font_size * 3))

                draw.text((x, y), full_text, font=font, fill="black")

                filename = f"meme_{random.randint(1000, 999999)}.png"
                output_path = os.path.join(self.output_dir, filename)
                img.save(output_path)

                return output_path

        except FileNotFoundError:
            raise ValueError(f"Image file not found: {path}")
        except OSError:
            raise ValueError(f"Cannot open or process image: {path}")
        except Exception as e:
            raise RuntimeError(f"Unexpected error during meme creation: {e}")


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
