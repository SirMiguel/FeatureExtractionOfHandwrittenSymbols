#
# from feature_extractor.features.ImageFeature import ImageFeature
#
# class ImagePixelsNeighboursImage(ImageFeature):
#     def __init__(self, null_pixel_value):
#         ImageFeature.__init__(self)
# #        self.pixel_neghbour_extractor =
#
#     def get_feature(self, image):
#         pixels_neighbours = []
#         for column in range(image.width):
#             for pixel in range(image.height):
#                 pixels_neighbours.append(self.get_neighbours_of_pixel(image, column, pixel))
#         return pixels_neighbours
#
#     def get_neighbours_of_pixel(self, image, pixel_x, pixel_y):
#         pixel_neighbours = self(image, pixel_x, pixel_y)
#         return pixel_neighbours
#
#
#
#
#                 # def does_pixel_have_neighbours(self, pixels_neighbours, pixel_neighbours_to_test, value_to_match):
#     #    for test_neighbour in pixel_neighbours_to_test:
#      #       self.pixel_neighbours[test_neighbour]
#       #      if not self.black_pixel.get_feature() :
#        #         return False
#         #return True
#
