class FavoriteShape:
    def __init__(self, color, shape):
        #self.color = color
        self.shape = shape

    @property
    def color(self):
        print('getter method for color')
        return self._color

    @color.setter
    def color(self, x):
        print('setter method for color')
        self._color = x

    @property
    def shape(self):
        print('getter method for shape')
        return self.something_else

    @shape.setter
    def shape(self, x):
        print('setter method for shape')
        self.something_else = x

obj1 = FavoriteShape('blue','square')
print('something_else = ' + obj1.something_else)
print('shape = ' + obj1.shape)