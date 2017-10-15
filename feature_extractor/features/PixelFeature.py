class PixelFeature:
    def __init__(self):
        pass

    def get_feature(self, pixel):
        raise NotImplementedError()

class MatchingColourFeature(PixelFeature):
    def __init__(self, pixel_colour):
        PixelFeature.__init__(self)
        self.pixel_colour = pixel_colour

    def get_feature(self, pixel):
        return self.pixel_colour == pixel

class NotMatchingColourFeature(PixelFeature):
    def __init__(self, pixel_colour):
        PixelFeature.__init__(self)
        self.pixel_colour = pixel_colour

    def get_feature(self, pixel):
        return self.pixel_colour != pixel