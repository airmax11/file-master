# Start the program
from PIL import Image

from geometry_figures import Square, Rectangle
from image_processing import Canvas

print("This is Canvas Application")
background_width = int(input("Enter background width: "))
background_height = int(input("Enter background height: "))
colors = {"white": (255, 255, 255), "black": (0, 0, 0)}
background_color = (input("Enter background color (Black/White): ")).lower()
canvas = Canvas(background_width, background_height, colors[background_color])


def _color():
    r = int(input("How much Red you want to have: "))
    g = int(input("How much Green you want to have: "))
    b = int(input("How much Blue you want to have: "))
    return r, g, b


while True:
    figure_shape = input("What figure you want to draw? (Square/Rectangle or Quit to end) :")
    if figure_shape.lower() == "quit":
        break
    if figure_shape.lower() == "square":
        square_x = int(input("Enter x: "))
        square_y = int(input("Enter y: "))
        square_side = int(input("Enter side: "))
        square_color = _color()
        square = Square(square_x, square_y, square_side, square_color)
        square.draw_square(canvas)

    if figure_shape.lower() == "rectangle":
        rec_x = int(input("Enter x: "))
        rec_y = int(input("Enter y: "))
        rec_h = int(input("Enter h: "))
        rec_w = int(input("Enter w: "))
        rec_color = _color()
        rectangle = Rectangle(rec_x, rec_y, rec_h, rec_w, rec_color)
        rectangle.draw_rectangle(canvas)

canvas.make_image()
