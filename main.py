from models.canvas import Canvas
from models.rectangle import Rectangle
from models.square import Square

if __name__ == '__main__':
    canvas_width = int(input('Enter canvas width: '))
    canvas_height = int(input('Enter canvas height: '))

    colors = {'white': (255, 255, 255), 'black': (0, 0, 0)}
    canvas_color = input('Enter canvas color (white or black): ')

    canvas = Canvas(height=canvas_height, width=canvas_width, color=colors[canvas_color])

    while True:
        shape = input('What do you like to draw? square or rectangle? type q to quit. ')
        if shape.lower() == 'rectangle':
            rx = int(input('Enter x of the rectangle: '))
            ry = int(input('Enter y of the rectangle: '))
            rw = int(input('Enter width of the rectangle: '))
            rh = int(input('Enter height of the rectangle: '))
            red = int(input('Enter red color value (between 0 and 255): '))
            green = int(input('Enter green color value (between 0 and 255): '))
            blue = int(input('Enter blue color value (between 0 and 255): '))

            r1 = Rectangle(x=rx, y=ry, height=rh, width=rw, color=(red, green, blue))
            r1.draw(canvas)

        if shape.lower() == 'square':
            sx = int(input('Enter x of the square: '))
            sy = int(input('Enter y of the square: '))
            side = int(input('Enter side of the square: '))
            red = int(input('Enter red color value (between 0 and 255): '))
            green = int(input('Enter green color value (between 0 and 255): '))
            blue = int(input('Enter blue color value (between 0 and 255): '))

            s1 = Square(x=1, y=3, side=3, color=(0, 100, 222))
            s1.draw(canvas)

        if shape.lower() == 'q':
            break

    canvas.make('canvas')
