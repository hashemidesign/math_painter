from typing import Dict, Tuple

from models.canvas import Canvas
from models.rectangle import Rectangle
from models.square import Square


def draw_shapes(canvas: Canvas, colors: Dict[str, Tuple[int, int, int]]) -> None:
    """
    Draw shapes on the canvas.

    Parameters:
    ----------
    - canvas (Canvas): The canvas object on which the shapes will be drawn.
    - colors (Dict[str, Tuple[int, int, int]]): A dictionary containing predefined colors.

    Returns:
    -------
    - None
    """
    while True:
        shape: str = input('What do you like to draw? square or rectangle? type q to quit. ')
        if shape.lower() == 'rectangle':
            rx: int = int(input('Enter x of the rectangle: '))
            ry: int = int(input('Enter y of the rectangle: '))
            rw: int = int(input('Enter width of the rectangle: '))
            rh: int = int(input('Enter height of the rectangle: '))
            red: int = int(input('Enter red color value (between 0 and 255): '))
            green: int = int(input('Enter green color value (between 0 and 255): '))
            blue: int = int(input('Enter blue color value (between 0 and 255): '))

            r1: Rectangle = Rectangle(x=rx, y=ry, height=rh, width=rw, color=(red, green, blue))
            r1.draw(canvas)

        if shape.lower() == 'square':
            sx: int = int(input('Enter x of the square: '))
            sy: int = int(input('Enter y of the square: '))
            side: int = int(input('Enter side of the square: '))
            red: int = int(input('Enter red color value (between 0 and 255): '))
            green: int = int(input('Enter green color value (between 0 and 255): '))
            blue: int = int(input('Enter blue color value (between 0 and 255): '))

            s1: Square = Square(x=sx, y=sy, side=side, color=(red, green, blue))
            s1.draw(canvas)

        if shape.lower() == 'q':
            break


if __name__ == '__main__':
    canvas_width: int = int(input('Enter canvas width: '))
    canvas_height: int = int(input('Enter canvas height: '))

    colors: Dict[str, Tuple[int, int, int]] = {'white': (255, 255, 255), 'black': (0, 0, 0)}
    canvas_color: str = input('Enter canvas color (white or black): ')

    canvas: Canvas = Canvas(height=canvas_height, width=canvas_width, color=colors[canvas_color])
    draw_shapes(canvas, colors)

    canvas.make('canvas')
