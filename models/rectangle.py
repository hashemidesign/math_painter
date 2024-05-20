import numpy as np
from typing import Tuple


class Rectangle:
    """
    A class representing a rectangle shape.

    Attributes:
    ----------
    - x (int): The x-coordinate of the top-left corner of the rectangle.
    - y (int): The y-coordinate of the top-left corner of the rectangle.
    - height (int): The height of the rectangle.
    - width (int): The width of the rectangle.
    - color (Tuple[int, int, int]): The RGB color tuple (0-255) to fill the rectangle.

    Methods:
    --------
    - draw(canvas: Canvas): Draws the square on the given canvas.
    """

    def __init__(self, x: int, y: int, height: int, width: int, color: Tuple[int, int, int]) -> None:
        self.x: int = x
        self.y: int = y
        self.height: int = height
        self.width: int = width
        self.color: Tuple[int, int, int] = color

    def draw(self, canvas: 'Canvas') -> None:
        """
        Draws the rectangle on the given canvas.

        Parameters:
        ----------
        - canvas (Canvas): The canvas object on which the rectangle will be drawn.

        Returns:
        --------
        - None
        """
        canvas.data[self.x: self.x + self.height, self.y: self.y + self.width] = self.color

