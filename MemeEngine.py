"""Image meme builder module using Pillow."""

import os
import random
from PIL import Image, ImageDraw, ImageFont


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

    def create(self, image_path, quote_text, quote_author, max_width=500):
        """
        Create a meme with text and author on the given image.

        Parameters:
        - image_path (str): Path to the input image
        - quote_text (str): The quote body to display
        - quote_author (str): The quote author to display
        - max_width (int): Optional max width of the meme image

        Returns:
        - str: Path to the generated meme image
        """
        try:
            with Image.open(image_path) as img:
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
            raise ValueError(f"Image file not found: {image_path}")
        except OSError:
            raise ValueError(f"Cannot open or process image: {image_path}")
        except Exception as e:
            raise RuntimeError(f"Unexpected error during meme creation: {e}")
