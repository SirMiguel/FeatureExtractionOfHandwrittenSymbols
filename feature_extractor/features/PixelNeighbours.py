from feature_extractor.features.PixelColour import PixelColour
from feature_extractor.features.ImageFeature import ImageFeature

class PixelNeighbours(ImageFeature):
    def __init__(self, null_pixel_value):
        ImageFeature.__init__(self)
        self.null_pixel_value = null_pixel_value

    def get_feature(self, image):
        neighbours_of_pixels = []
        for pixel_x in range(image.get_width()):
            neighbours_of_pixels.append([self.get_neighbours(image, pixel_x, pixel_y) for pixel_y in range(image.get_height())])
        return neighbours_of_pixels
#get brightest layer

    def get_neighbours(self, image, pixel_x, pixel_y):
        neighbours = dict()
        neighbours.update({"upper": self.get_upper_neighbour(image, pixel_x, pixel_y)})
        neighbours.update({"upper-left": self.get_upper_left_neighbour(image, pixel_x, pixel_y)})
        neighbours.update({"upper-right": self.get_upper_right_neighbour(image, pixel_x, pixel_y)})
        neighbours.update({"left": self.get_left_neighbour(image, pixel_x, pixel_y)})
        neighbours.update({"right": self.get_right_neighbour(image, pixel_x, pixel_y)})
        neighbours.update({"lower": self.get_lower_neighbour(image, pixel_x, pixel_y)})
        neighbours.update({"lower-left": self.get_lower_left_neighbour(image, pixel_x, pixel_y)})
        neighbours.update({"lower-right": self.get_lower_right_neighbour(image, pixel_x, pixel_y)})
        return neighbours

    def get_upper_neighbour(self, image, pixel_x, pixel_y):
        if self.is_pixel_top_border(pixel_y):
            return self.null_pixel_value
        else:
            return image.get_pixel(pixel_x, pixel_y -1)
        #TODO check later if need to add get value

    def get_upper_left_neighbour(self, image, pixel_x, pixel_y):
        if self.is_pixel_left_border(pixel_x) or self.is_pixel_top_border(pixel_y):
            return self.null_pixel_value
        else:
            return image.get_pixel(pixel_x - 1, pixel_y - 1)
        #TODO check later if need to add get value

    def get_upper_right_neighbour(self, image, pixel_x, pixel_y):
        if self.is_pixel_right_border(image.get_width(), pixel_x) or self.is_pixel_top_border(pixel_y):
            return self.null_pixel_value
        else:
            return image.get_pixel(pixel_x + 1, pixel_y - 1)
        #TODO check later if need to add get value

    def get_right_neighbour(self, image, pixel_x, pixel_y):
        if self.is_pixel_right_border(image.get_width(), pixel_x):
            return self.null_pixel_value
        else:
            return image.get_pixel(pixel_x + 1, pixel_y)
        #TODO check later if need to add get value

    def get_left_neighbour(self, image, pixel_x, pixel_y):
        if self.is_pixel_left_border(pixel_x):
            return self.null_pixel_value
        else:
            return image.get_pixel(pixel_x - 1, pixel_y)
            # TODO check later if need to add get value

    def get_lower_right_neighbour(self, image, pixel_x, pixel_y):
        if self.is_pixel_right_border(image.get_width(), pixel_x) or self.is_pixel_bottom_border(image.get_width(), pixel_y):
            return self.null_pixel_value
        else :
            return image.get_pixel(pixel_x + 1, pixel_y + 1)
        #TODO check later if need to add get value

    def get_lower_neighbour(self, image, pixel_x, pixel_y):
        if self.is_pixel_bottom_border(image.get_width(), pixel_y):
            return self.null_pixel_value
        else:
            return image.get_pixel(pixel_x, pixel_y + 1)
        #TODO check later if need to add get value

    def get_lower_left_neighbour(self, image, pixel_x, pixel_y):
        if self.is_pixel_left_border(pixel_x) or self.is_pixel_bottom_border(image.get_width(), pixel_y):
            return self.null_pixel_value
        else :
            return image.get_pixel(pixel_x - 1, pixel_y + 1)
        #TODO check later if need to add get value

    def is_pixel_top_border(self, pixel_y):
        return pixel_y == 0

    def is_pixel_bottom_border(self, image_height, pixel_y):
        return pixel_y == image_height - 1

    def is_pixel_left_border(self, pixel_x):
        return pixel_x == 0

    def is_pixel_right_border(self, image_width, pixel_x):
        return pixel_x == image_width - 1

  #  def is_pixel_top_left_border(self, pixel_x, pixel_y):
   #     return self.is_pixel_top_border(pixel_y) and self.is_pixel_left_border(pixel_x)

#    def is_pixel_top_right_border(self, image_width, pixel_x, pixel_y):
 #       return self.is_pixel_top_border(pixel_y) and self.is_pixel_right_border(image_width, pixel_x)

#    def is_pixel_bottom_left_border(self, pixel_x, pixel_y):
 #       return self.is_pixel_bottom_border(pixel_y) and self.is_pixel_left_border(pixel_x)

#    def is_pixel_bottom_right_border(self,image_width ,pixel_x, pixel_y):
 #       return self.is_pixel_bottom_border(pixel_y) and self.is_pixel_right_border(image_width, pixel_x)



# class ColouredPixelNeighbours(PixelNeighbours):
#     def __init__(self, null_pixel_value, colour_to_match):
#         PixelNeighbours.__init__(self, null_pixel_value)
#         self.colour_to_match = PixelColour(colour_to_match)
#
#     def get_feature(self, image, pixel_x, pixel_y):
#         pixel_neighbours = PixelNeighbours.get_feature(self, image, pixel_x, pixel_y)
#         coloured_pixel_neighbours = dict()
#         if self.has_coloured_neighbours(pixel_neighbours):
#             for pixel_neighbour in pixel_neighbours:
#                 if self.colour_to_match.get_feature(pixel_neighbour):
#                     coloured_pixel_neighbours.update(pixel_neighbour)
#
#
#     def has_coloured_neighbours(self, pixel_neighbours):
#         for pixel_neighbour in pixel_neighbours:
#             if self.colour_to_match.get_feature(pixel_neighbour):
#                 return True
