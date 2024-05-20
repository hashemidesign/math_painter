from typing import Tuple


class Square:
    """
    A class representing a square shape.

    Attributes:
    ----------
    - x (int): The x-coordinate of the top-left corner of the square.
    - y (int): The y-coordinate of the top-left corner of the square.
    - side (int): The length of each side of the square.
    - color (Tuple[int, int, int]): The RGB color tuple (0-255) to fill the square.

    Methods:
    --------
    - draw(canvas: Canvas): Draws the square on the given canvas.
    """

    def __init__(self, x: int, y: int, side: int, color: Tuple[int, int, int]) -> None:
        self.x: int = x
        self.y: int = y
        self.side: int = side
        self.color: Tuple[int, int, int] = color

    def draw(self, canvas: 'Canvas') -> None:
        """
        Draws the square on the given canvas.

        Parameters:
        ----------
        - canvas (Canvas): The canvas object on which the square will be drawn.

        Returns:
        -------
        - None
        """
        canvas.data[self.x: self.x + self.side, self.y: self.y + self.side] = self.color
