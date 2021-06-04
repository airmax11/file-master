class Square:

    def __init__(self, x, y, side, color):
        self.color = color
        self.side = side
        self.y = y
        self.x = x

    def draw_square(self, canvas):
        canvas.data[self.x: self.x + self.side, self.y: self.y + self.side] = self.color


class Rectangle:

    def __init__(self, x, y, height, width,  color):
        self.color = color
        self.width = width
        self.y = y
        self.x = x
        self.height = height

    def draw_rectangle(self, canvas):
        canvas.data[self.x: self.x + self.height, self.y: self.y + self.width] = self.color
