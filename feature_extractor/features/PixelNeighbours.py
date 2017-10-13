class PixelNeighbours:
    def __init__(self, null_pixel_value):
        self.null_pixel_value = null_pixel_value

    def get_feature(self, image, pixel_x, pixel_y):
        return self.get_neighbours(image, pixel_x, pixel_y)

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

    #Methods for future use maybe, currently unused
    def is_pixel_top_border(self, pixel_y):
        return pixel_y == 0

    def is_pixel_bottom_border(self, image_height, pixel_y):
        return pixel_y == image_height - 1

    def is_pixel_left_border(self, pixel_x):
        return pixel_x == 0

    def is_pixel_right_border(self, image_width, pixel_x):
        return pixel_x == image_width - 1