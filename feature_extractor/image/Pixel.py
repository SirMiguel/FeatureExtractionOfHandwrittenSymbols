
class Pixel:

    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value

class BlackPixel(Pixel):
    def __init__(self):
        Pixel.__init__(self, 1)

class WhitePixel(Pixel):
    def __init__(self):
        Pixel.__init__(self, 0)