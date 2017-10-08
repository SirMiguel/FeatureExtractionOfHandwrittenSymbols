from feature_extractor.features.PixelFeature import PixelFeature
from feature_extractor.image.Pixel import Pixel

class PixelColour(PixelFeature):
    def __init__(self, pixel_value):
        PixelFeature.__init__(self)
        self.pixel_value = pixel_value

    def get_feature(self, pixel_value):
        return pixel_value == self.pixel_value

class PixelBlack(PixelColour):
    def __init__(self):
        PixelColour.__init__(self, Pixel(0))


