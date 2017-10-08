from feature_extractor.image.Pixel import Pixel
class SelfAwarePixel(Pixel):
    def __init__(self, position_x, position_y, colour, neighbours):
        Pixel.__init__(self, colour)
        self.neighbours = neighbours
        self.position_x = position_x
        self.position_y = position_y

    def get_neighbours(self):
        return self.neighbours

    def get_position_x(self):
        return self.position_x

    def get_position_y(self):
        return self.position_y