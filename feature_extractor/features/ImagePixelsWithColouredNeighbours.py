# from feature_extractor.features.ImagePixelsWithNeighbours import ImagePixelsNeighboursImage
# from feature_extractor.features.PixelColour import PixelColour
# from feature_extractor.features.ImageFeature import ImageFeature
#
#
# class ImagePixelsWithColouredNeighbours(ImagePixelsNeighboursImage):
#     def __init__(self, null_pixel_value, pixel_value_to_match):
#         ImagePixelsNeighboursImage.__init__(self, null_pixel_value)
#         self.colour_to_match = PixelColour(pixel_value_to_match)
#
#     def get_feature(self, image):
#         pixels_neighbours = ImagePixelsNeighboursImage.get_feature(self, image)
#         pixels_with_neighbours_of_value = []
#         for pixel_neighbours in pixels_neighbours:
#
#             if self.is_pixel_neighbours_of_value(pixel_neighbours):
#                 pixels_with_neighbours_of_value.append(pixel_neighbours)
#
#         return pixels_with_neighbours_of_value
#
#     def is_pixel_neighbours_of_value(self, pixel_neighbours):
#         for neighbour, pixel_colour in pixel_neighbours.items():
#              if self.colour_to_match.does_pixel_match_feature(pixel_colour):
#                  return True
#         return False
#
# class ImagePixelsOnlyColouredNeighbours(ImagePixelsWithColouredNeighbours):
#
#     def __init__(self, null_pixel_value, colour_to_match):
#         ImagePixelsWithColouredNeighbours.__init__(self, null_pixel_value, colour_to_match)
#
#     def get_feature(self, image):
#         pixels_with_coloured_neighbours = ImagePixelsWithColouredNeighbours.get_feature(self, image)
#         pixels_with_only_coloured_neighbours = []
#         for pixel_neighbours in pixels_with_coloured_neighbours:
#             pixels_with_only_coloured_neighbours.append(self.get_only_coloured_neighbours(pixel_neighbours))
#         return pixels_with_only_coloured_neighbours
#
#
#     def get_only_coloured_neighbours(self, neighbours):
#         coloured_pixels = dict()
#         for neighbour, pixel in neighbours.items():
#             if self.colour_to_match.does_pixel_match_feature(pixel):
#                 coloured_pixels.update({neighbour : pixel})
#         return coloured_pixels
#
#
#         # pixels_neighbours = ImagePixelsNeighboursImage.get_feature(self, image)
#         # pixels_with_amount_matching_neighbours = []
#         # for pixel_neighbours in pixels_neighbours:
#         #     amount_of_matching_pixels = self.get_amount_of_matching_pixels(pixel_neighbours)
#         #
#         #     if amount_of_matching_pixels <= self.amount_of_neighbours_matching:
#         #         pixels_with_amount_matching_neighbours.append(pixels_neighbours)
#         # return pixels_with_amount_matching_neighbours
#
#     def has_coloured_neighbours(self, pixel_neighbours):
#         for neighbour, pixel_value in pixel_neighbours.items():
#             if self.colour_to_match.does_pixel_match_feature(pixel_value):
#                 return True
#
#     # def get_amount_of_matching_pixels(self, pixel_neighbours):
#     #     amount_of_matching_pixels = 0
#     #     for pixel_neighbour in pixel_neighbours:
#     #         if self.colour_to_match.get_feature(pixel_neighbour):
#     #             amount_of_matching_pixels += 1
#     #     return amount_of_matching_pixels
#
#
# #class ImagePixelsOnlyColouredNeighboursLimit(ImagePixelsOnlyColouredNeighbours):
#  #       def __init__(self, null_pixel_value, colour_to_match, coloured_pixel_limit):
#   #          ImagePixelsOnlyColouredNeighbours.__init__(self, null_pixel_value, colour_to_match)
#    #         self.coloured_pixel_limit = coloured_pixel_limit
#
#     #    def get_feature(self, image):
#      #       coloured_pixel_neighbours = 0
#
# class ColouredPixelsWithColouredNeighbours(ImagePixelsOnlyColouredNeighbours):
#     def __init__(self, null_pixel_value, pixel_colour, neighbour_colour):
#         ImagePixelsOnlyColouredNeighbours.__init__(self, null_pixel_value, neighbour_colour)
#
#     def get_feature(self, image):
#         coloured_pixels_with_coloured_neighbours = []
#         for column in range(image.get_width()):
#             for pixel in range(image.get_height()):
#                 if self.colour_to_match.does_pixel_match_feature(image.get_pixel(column, pixel)):
#                     coloured_pixel_neighbours = self.get_only_coloured_neighbours(self.get_neighbours_of_pixel(image, column, pixel))
#                     coloured_pixels_with_coloured_neighbours.append(coloured_pixel_neighbours)
#         return coloured_pixels_with_coloured_neighbours
#
# #class ColouredPixelsWithAtMostColouredNeighbours(ColouredPixelsWithColouredNeighbours):
#     #def __init__(self, null_pixel_value, pixel_colour, neighbour_colour, neighbour_condition):
#
# #
# # class ColouredPixelsColouredNeighbours(ImageFeature):
# #     def __init__(self, pixel_colour_feature, neighbours_colour_feature, null_pixel_value):
# #         ImageFeature.__init__(self)
# #         self.coloured_neighbour_extractor = PixelColouredNeighbours(neighbours_colour_feature, null_pixel_value)
# #         self.coloured_pixel_feature = pixel_colour_feature
# #
# #     def get_feature(self, image):
# #         pixel_features = []
# #         for pixel_x in range(image.get_width()):
# #             for pixel_y in range(image.get_height()):
# #                 image_pixel = image.get_pixel(pixel_x, pixel_y)
# #                 if self.coloured_pixel_feature.does_pixel_match_feature(image_pixel):
# #                     pixel_features.append(self.coloured_neighbour_extractor.get_feature(image))
# #         return pixel_features
# #
