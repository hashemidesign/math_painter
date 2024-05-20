from typing import Tuple

import numpy as np
from PIL import Image


class Canvas:
    """
    A class representing a customizable canvas for drawing.

    Attributes:
    ----------
    - height (int): The height of the canvas in pixels.
    - width (int): The width of the canvas in pixels.
    - color (tuple): The RGB color tuple (0-255) to fill the canvas.

    Methods:
    --------
    - make(filename): Saves the canvas as a PNG image.
    """

    def __init__(self, height: int, width: int, color: Tuple[int, int, int]) -> None:
        self.height = height
        self.width = width
        self.color = color

        # Create an empty canvas with the specified height, width, and color
        self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        self.data[:] = self.color

    def make(self, filename: str):
        """
        Save the canvas as a PNG image.

        Parameters:
        ----------
        - filename (str): Name of the output image file (without extension).

        Returns:
        -------
        - None
        """
        img = Image.fromarray(self.data, mode='RGB')
        img.save(f'output/{filename}.png')
