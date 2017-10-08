# from feature_extractor.features.ImageFeature import ImageFeature
# from feature_extractor.features.PixelColour import PixelColour
#
# class ImageColouredPixelsFeature(ImageFeature):
#     def __init__(self, colour_to_get):
#         ImageFeature.__init__(self)
#         self.matching_colour = PixelColour(colour_to_get)
#
#     def get_feature(self, image):
#         matching_pixels = []
#         for column in image.get_pixels():
#             for pixel in column:
#                 if self.matching_colour.does_pixel_match_feature(pixel):
#                     matching_pixels.append(pixel)
#         return matching_pixels