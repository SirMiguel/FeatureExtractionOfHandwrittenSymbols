# from feature_extractor.features.PixelFeature import PixelFeature
# from feature_extractor.image.Pixel import Pixel
#
# class PixelColour(PixelFeature):
#     def __init__(self, pixel_value):
#         PixelFeature.__init__(self)
#         self.pixel_value = pixel_value
#
#     def does_pixel_match_feature(self, pixel):
#         return pixel == self.pixel_value.get_colour()
#
# class BlackPixel(PixelColour):
#     def __init__(self):
#         PixelColour.__init__(self, Pixel(1))
#
# class WhitePixel(PixelColour):
#     def __init__(self):
#         PixelColour.__init__(self, Pixel(0))
#
#
