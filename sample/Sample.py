
class Sample:
    def __init__(self, sample_code, sample_number, sample_image):
        self.sample_code = sample_code
        self.sample_number = sample_number
        self.sample_image = sample_image

    def get_pixel_vector(self):
        return [self.sample_image[x][y] for y in range(len(self.sample_image[0])) for x in range(len(self.sample_image))]