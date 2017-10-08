
class Image:

    def __init__(self, pixels, image_width, image_height):
        self.pixels = pixels
        self.width = image_width
        self.height = image_height

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_pixels(self):
        return self.pixels

    def get_pixel(self, pixel_x, pixel_y):
        pixel = self.pixels[pixel_y][pixel_x]
        return pixel

 #   def get_pixel_vector(self):
  #      return [pixel for column in self.pixels for pixel in column]

