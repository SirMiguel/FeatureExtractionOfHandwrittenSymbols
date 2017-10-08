
class Pixel:
    def __init__(self, colour):
        self.value = colour

    def get_colour(self):
        return self.value

class BlackPixel(Pixel):
    def __init__(self):
        Pixel.__init__(self, 1)


class WhitePixel(Pixel):
    def __init__(self):
        Pixel.__init__(self, 0)