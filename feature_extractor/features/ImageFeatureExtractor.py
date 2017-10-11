from feature_extractor.features.PixelNeighbours import PixelNeighbours
from feature_extractor.features.SelfAwarePixel import SelfAwarePixel

class PixelFeatureExtractor:
    def __init__(self):
        pass

    def get_feature(self, pixel):
        raise NotImplementedError()

#class PixelNeighbourFeature:


class MatchingColourFeatureExtractor(PixelFeatureExtractor):
    def __init__(self, pixel_colour):
        PixelFeatureExtractor.__init__(self)
        self.pixel_colour = pixel_colour

    def get_feature(self, pixel):
        return self.pixel_colour == pixel

class NotMatchingColourFeatureExtractor(PixelFeatureExtractor):
    def __init__(self, pixel_colour):
        PixelFeatureExtractor.__init__(self)
        self.pixel_colour = pixel_colour

    def get_feature(self, pixel):
        return self.pixel_colour != pixel


#IMAGE FEATRURES

class ImageFeatureExtractor:
    def __init__(self, null_pixel_value):
        self.neighbour_extractor = PixelNeighbours(null_pixel_value)

    def get_feature(self, image):
        selfaware_pixels = []
        for pixel_x in range(image.get_width()):
            for pixel_y in range(image.get_height()):
                pixel = image.get_pixel(pixel_x, pixel_y)
                pixel_neighbours = self.neighbour_extractor.get_feature(image, pixel_x, pixel_y)
                selfaware_pixels.append(SelfAwarePixel(pixel_x, pixel_y, pixel, pixel_neighbours))
        return selfaware_pixels


class ColouredPixelsExtractor(ImageFeatureExtractor):
    def __init__(self, pixel_colour, null_pixel_colour):
        ImageFeatureExtractor.__init__(self, null_pixel_colour)
        self.pixel_colour_feature = MatchingColourFeatureExtractor(pixel_colour)

    def get_feature(self, image):
        coloured_pixels = []
        for selfaware_pixel in ImageFeatureExtractor.get_feature(self, image):
            if self.pixel_colour_feature.get_feature(selfaware_pixel.get_colour()):
                coloured_pixels.append(selfaware_pixel)
        return coloured_pixels


class ColouredPixelsWithColouredNeighboursExtractor(ColouredPixelsExtractor):
    def __init__(self, pixel_colour, neighbour_colour,  null_pixel_value):
        ColouredPixelsExtractor.__init__(self, pixel_colour, null_pixel_value)
        self.neighbour_colour_feature = MatchingColourFeatureExtractor(neighbour_colour)


    def get_feature(self, image):
        coloured_pixels_coloured_neighbours = self.get_coloured_pixels_coloured_neighbours(image)
        return coloured_pixels_coloured_neighbours

    def get_coloured_pixels_coloured_neighbours(self, image):
        coloured_pixels_coloured_neighbours = []
        coloured_pixels = ColouredPixelsExtractor.get_feature(self, image)
        for coloured_selfaware_pixel in coloured_pixels:
            if self.does_pixel_have_coloured_neighbours(coloured_selfaware_pixel.get_neighbours()):
                coloured_pixels_coloured_neighbours.append(coloured_selfaware_pixel)
        return coloured_pixels_coloured_neighbours

    def does_pixel_have_coloured_neighbours(self, pixel_neighbours):
        for pixel_neighbour, neighbour_colour in pixel_neighbours.items():
            if self.neighbour_colour_feature.get_feature(neighbour_colour):
                return True
        return False

    def get_coloured_neighbours(self, neighbours):
        coloured_neighbours = dict()
        for neighbour_name, neighbour_pixel in neighbours.items():
            if self.neighbour_colour_feature.get_feature(neighbour_pixel):
                coloured_neighbours.update({neighbour_name : neighbour_pixel})
        return coloured_neighbours

class ColouredPixelsWithColouredNamedNeighboursExtractor(ColouredPixelsWithColouredNeighboursExtractor):
    def __init__(self, pixel_colour, neighbour_pixel_colour, neighbour_names_to_match, null_pixel_value):
        ColouredPixelsWithColouredNeighboursExtractor.__init__(self, pixel_colour, neighbour_pixel_colour, null_pixel_value)
        self.neighbours_names_to_match = neighbour_names_to_match

    def get_feature(self, image):
        pixels = ColouredPixelsWithColouredNeighboursExtractor.get_feature(self, image)
        matched_pixels = []
        for coloured_selfware_pixel in pixels:
            if self.do_pixels_specified_neighbours_match(coloured_selfware_pixel.get_neighbours()):
                matched_pixels.append(coloured_selfware_pixel)
        return matched_pixels

    def do_pixels_specified_neighbours_match(self, pixel_neighbours):
        for neighbour_name in self.neighbours_names_to_match:
            if not self.pixel_colour_feature.get_feature(pixel_neighbours[neighbour_name]):
                return False
        return True


class ColouredPixelsWithBoundariedWithColouredNeighbours(ColouredPixelsWithColouredNeighboursExtractor):
    def __init__(self, pixel_colour, neighbour_pixel_colour, coloured_neighbour_limit, null_pixel_value):
        ColouredPixelsWithColouredNeighboursExtractor.__init__(self, pixel_colour, neighbour_pixel_colour, null_pixel_value)
        self.coloured_neighbour_boundary = coloured_neighbour_limit

    def get_feature(self, image):
        pixels = ColouredPixelsWithColouredNeighboursExtractor.get_feature(self, image)
        matched_pixels = []
        for coloured_selfware_pixel in pixels:
            if self.does_coloured_neighbours_match_boundary(coloured_selfware_pixel.get_neighbours()):
                matched_pixels.append(coloured_selfware_pixel)
        return matched_pixels

    def does_coloured_neighbours_match_boundary(self, pixel_neighbours):
        raise NotImplementedError("Must write child class to implement the boundary condition")

    def get_number_of_matching_neighbours(self, pixel_neighbours):
        number_of_coloured_neighbours = 0
        for neighbour, neighbour_colour in pixel_neighbours.items():
            if self.pixel_colour_feature.get_feature(neighbour_colour):
                number_of_coloured_neighbours += 1
        return number_of_coloured_neighbours


class ColouredPixelsWithAtMostColouredNeighbours(ColouredPixelsWithBoundariedWithColouredNeighbours):
    def __init__(self, pixel_colour, neighbour_pixel_colour, coloured_neighbour_limit, null_pixel_value):
        ColouredPixelsWithBoundariedWithColouredNeighbours.__init__(self, pixel_colour, neighbour_pixel_colour, coloured_neighbour_limit, null_pixel_value)

    def does_coloured_neighbours_match_boundary(self, pixel_neighbours):
        return self.get_number_of_matching_neighbours(pixel_neighbours) <= self.coloured_neighbour_boundary


class ColouredPixelsWithExactlyAsManyColouredNeighbours(ColouredPixelsWithBoundariedWithColouredNeighbours):
    def __init__(self, pixel_colour, neighbour_pixel_colour, coloured_neighbour_limit, null_pixel_value):
        ColouredPixelsWithBoundariedWithColouredNeighbours.__init__(self, pixel_colour, neighbour_pixel_colour, coloured_neighbour_limit, null_pixel_value)

    def does_coloured_neighbours_match_boundary(self, pixel_neighbours):
        return self.get_number_of_matching_neighbours(pixel_neighbours) == self.coloured_neighbour_boundary

class ColouredPixelsWithAtLeastAsManyColouredNeighbours(ColouredPixelsWithBoundariedWithColouredNeighbours):
    def __init__(self, pixel_colour, neighbour_pixel_colour, coloured_neighbour_limit, null_pixel_value):
        ColouredPixelsWithBoundariedWithColouredNeighbours.__init__(self, pixel_colour, neighbour_pixel_colour, coloured_neighbour_limit, null_pixel_value)

    def does_coloured_neighbours_match_boundary(self, pixel_neighbours):
        return self.get_number_of_matching_neighbours(pixel_neighbours) >= self.coloured_neighbour_boundary

class ColouredPixelsWithNoNamedColouredNeighbours(ColouredPixelsExtractor):
    def __init__(self, pixel_colour, neighbours_to_check, neighbour_colour_not_allowed, null_pixel_value):
        ColouredPixelsExtractor.__init__(self, pixel_colour, null_pixel_value)
        self.neighbour_forbidden_colour_feature = NotMatchingColourFeatureExtractor(neighbour_colour_not_allowed)
        self.neighbours_without_colour = neighbours_to_check

    def get_feature(self, image):
        coloured_selfaware_pixels = ColouredPixelsExtractor.get_feature(self, image)
        pixels_not_containing_neighbours_with_forbidden_colour = []
        for coloured_selfaware_pixel in coloured_selfaware_pixels:
            if self.check_neighbours_do_not_contain_forbidden_colour(coloured_selfaware_pixel.get_neighbours()):
                pixels_not_containing_neighbours_with_forbidden_colour.append(coloured_selfaware_pixel)
        return pixels_not_containing_neighbours_with_forbidden_colour


    def check_neighbours_do_not_contain_forbidden_colour(self, pixel_neighbours):
        for neighbour_to_check in self. neighbours_without_colour:
            if self.does_pixel_contain_forbidden_colour(pixel_neighbours[neighbour_to_check]) :
                return False
        return True

    def does_pixel_contain_forbidden_colour(self, pixel):
        return not self.neighbour_forbidden_colour_feature.get_feature(pixel)


class ComplexImageFeatureExtractor(ImageFeatureExtractor):
    def __init__(self, image_features, null_pixel_value):
        ImageFeatureExtractor.__init__(self, null_pixel_value)
        self.image_features = image_features

    def get_feature(self, image):
        raise NotImplementedError("Complex Image Features must be derived from.")

    def get_all_image_feature_vectors(self, image):
        image_feature_vectors = []
        for image_feature in self.image_features:
            image_feature_vectors.append(image_feature.get_feature(image))
        return image_feature_vectors

class ORComplexImageFeature(ComplexImageFeatureExtractor):
    def __init__(self, image_features, null_pixel_value):
        ComplexImageFeatureExtractor.__init__(self, image_features, null_pixel_value)

    def get_feature(self, image):
        image_feature_vectors = self.get_all_image_feature_vectors(image)
        or_features_vector = []
        for image_feature_vector in image_feature_vectors:
            or_features_vector.extend(feature for feature in image_feature_vector if feature not in or_features_vector)
            #or_features_vector = list(set(or_features_vector + image_feature_vector))
        return or_features_vector

class MinusSumComplexImageFeature(ComplexImageFeatureExtractor):
    def __init__(self, image_features, null_pixel_value):
        assert len(image_features) >= 2
        ComplexImageFeatureExtractor.__init__(self, image_features, null_pixel_value)

    def get_feature(self, image):
        image_feature_vectors = self.get_all_image_feature_vectors(image)
        minus_sum_of_features = len(image_feature_vectors[0])
        for image_feature_vector in image_feature_vectors[1:]:
            minus_sum_of_features -= len(image_feature_vector)
        return minus_sum_of_features

class ColourPixelsInRowsFeatureExtractor(ColouredPixelsExtractor):
    def __init__(self, pixel_colour, null_pixel_value):
        ColouredPixelsExtractor.__init__(self, pixel_colour, null_pixel_value)

    def get_feature(self, image):
        selfaware_colour_pixels = ColouredPixelsExtractor.get_feature(self, image)
        coloured_pixels_in_rows = []
        for row in range(image.get_height()):
            coloured_pixels_in_row = []
            for colour_pixel in selfaware_colour_pixels:
                if colour_pixel.get_position_y() == row:
                    coloured_pixels_in_row.append(colour_pixel)
            coloured_pixels_in_rows.append(coloured_pixels_in_row)
        return coloured_pixels_in_rows

class AmountOfColourPixelsInRowsFeatureExtractor(ColourPixelsInRowsFeatureExtractor):
    def __init__(self, pixel_colour, null_pixel_value):
        ColourPixelsInRowsFeatureExtractor.__init__(self, pixel_colour, null_pixel_value)

    def get_feature(self, image):
        colour_pixels_in_each_row = ColourPixelsInRowsFeatureExtractor.get_feature(self, image)
        return [len(colour_pixels_in_row) for colour_pixels_in_row in colour_pixels_in_each_row]

class RowsWithAtLeastQuantityOfColourPixelsFeatureExtractor(AmountOfColourPixelsInRowsFeatureExtractor):
    def __init__(self, amount_of_colour_pixels_in_row, pixel_colour, null_pixel_value):
        AmountOfColourPixelsInRowsFeatureExtractor.__init__(self, pixel_colour, null_pixel_value)
        self.amount_of_colour_pixels_in_row = amount_of_colour_pixels_in_row

    def get_feature(self, image):
        amount_of_colour_pixels_in_each_row = AmountOfColourPixelsInRowsFeatureExtractor.get_feature(self, image)
        rows_with_amount_of_colour_pixels = dict()
        for row_index in range(len(amount_of_colour_pixels_in_each_row)):
            amount_of_colour_pixels_in_row = amount_of_colour_pixels_in_each_row[row_index]
            if amount_of_colour_pixels_in_row >= self.amount_of_colour_pixels_in_row:
                rows_with_amount_of_colour_pixels.update({row_index : amount_of_colour_pixels_in_row})
        return rows_with_amount_of_colour_pixels

class ColourPixelsInColumnsFeatureExtractor(ColouredPixelsExtractor):
    def __init__(self, pixel_colour, null_pixel_value):
        ColouredPixelsExtractor.__init__(self, pixel_colour, null_pixel_value)

    def get_feature(self, image):
        selfaware_colour_pixels = ColouredPixelsExtractor.get_feature(self, image)
        coloured_pixels_in_columns = []
        for column in range(image.get_width()):
            coloured_pixels_in_column = []
            for colour_pixel in selfaware_colour_pixels:
                if colour_pixel.get_position_x() == column:
                    coloured_pixels_in_column.append(colour_pixel)
            coloured_pixels_in_columns.append(coloured_pixels_in_column)
        return coloured_pixels_in_columns

class AmountOfColourPixelsInColumnsFeatureExtractor(ColourPixelsInColumnsFeatureExtractor):
    def __init__(self, pixel_colour, null_pixel_value):
        ColourPixelsInColumnsFeatureExtractor.__init__(self, pixel_colour, null_pixel_value)

    def get_feature(self, image):
        colour_pixels_in_each_columns = ColourPixelsInColumnsFeatureExtractor.get_feature(self, image)
        return [len(colour_pixels_in_column) for colour_pixels_in_column in colour_pixels_in_each_columns]

class ColumnsWithAtLeastQuantityOfColourPixelsFeatureExtractor(AmountOfColourPixelsInColumnsFeatureExtractor):
    def __init__(self, amount_of_colour_pixels_in_column, pixel_colour, null_pixel_value):
        AmountOfColourPixelsInColumnsFeatureExtractor.__init__(self, pixel_colour, null_pixel_value)
        self.amount_of_colour_pixels_in_column = amount_of_colour_pixels_in_column

    def get_feature(self, image):
        amount_of_colour_pixels_in_each_column = AmountOfColourPixelsInColumnsFeatureExtractor.get_feature(self, image)
        columns_with_amount_of_colour_pixels = dict()
        for row_index in range(len(amount_of_colour_pixels_in_each_column)):
            amount_of_colour_pixels_in_column = amount_of_colour_pixels_in_each_column[row_index]
            if amount_of_colour_pixels_in_column >= self.amount_of_colour_pixels_in_column:
                columns_with_amount_of_colour_pixels.update({row_index : amount_of_colour_pixels_in_column})
        return columns_with_amount_of_colour_pixels


class ConnectedColourRegionsInImage(ColouredPixelsExtractor):
    def __init__(self, pixel_colour, null_pixel_value):
        ColouredPixelsExtractor.__init__(self, pixel_colour, null_pixel_value)
        self.neighbour_extractor = PixelNeighbours(null_pixel_value)

    def get_feature(self, image):
        coloured_pixels = ColouredPixelsExtractor.get_feature(self, image)
        pixel_blobs = []

        for pixel in coloured_pixels:
            if self.is_new_blob(pixel, pixel_blobs):
                new_blob = [pixel]
                blob_coloured_neighbours = self.get_coloured_neighbours_as_selfaware_pixels(image, pixel)

                while blob_coloured_neighbours:
                    current_pixel = blob_coloured_neighbours.pop()
                    new_blob.append(current_pixel)
                    current_pixels_neighbours = self.get_coloured_neighbours_as_selfaware_pixels(image, current_pixel)

                    blob_coloured_neighbours.extend(self.get_selfaware_neighbours_not_in_blob(current_pixels_neighbours, new_blob))
                pixel_blobs.append(new_blob)
        return pixel_blobs

    def is_new_blob(self, pixel, pixel_blobs):
        new_blob = True
        for pixel_blob in pixel_blobs:
            for blob_pixel in pixel_blob:
                if pixel.get_position_x() == blob_pixel.get_position_x() and pixel.get_position_y() == blob_pixel.get_position_y():
                    new_blob = False
        return new_blob

    def get_selfaware_neighbours_not_in_blob(self, neighbours, blob):
        selfaware_neighbours = []
        for neighbour in neighbours:
            if self.pixel_colour_feature.get_feature(neighbour.get_colour()):
                neighbour_x = neighbour.get_position_x()
                neighbour_y = neighbour.get_position_y()
                neighbour_in_blob = False
                for pixel in blob:
                    if pixel.get_position_x() == neighbour_x and pixel.get_position_y() == neighbour_y:
                        neighbour_in_blob = True
                if not neighbour_in_blob:
                    selfaware_neighbours.append(neighbour)
        return selfaware_neighbours

    #def has_coloured_neighbour
    def get_coloured_neighbours_as_selfaware_pixels(self, image, pixel):
        selfaware_neighbours = []
        for neighbour_name, neighbour_colour in pixel.neighbours.items():
            if self.pixel_colour_feature.get_feature(neighbour_colour):
                neighbour_x = pixel.get_neighbour_position_x(neighbour_name)
                neighbour_y = pixel.get_neighbour_position_y(neighbour_name)
                selfaware_neighbours.append(SelfAwarePixel(neighbour_x,
                                                           neighbour_y,
                                                           neighbour_colour,
                                                           self.neighbour_extractor.get_neighbours(image, neighbour_x, neighbour_y)))
        return selfaware_neighbours


        # for each pixel check all current blobs to see if it is in there
            # if not add pixel to new blob,
            # add to pixel neighbours to blob neighbours
            # while blob neighbours:
                # get the neighbours neighbour:
                # if they are of the same colour add them to the new blob
                # add neighbours to blob neighbours

    def do_pixel_positions_match(self, neighbour_x, neighbour_y, pixel):
        return pixel.get_position_x() == neighbour_x and pixel.get_position_y() == neighbour_y

    def get_coloured_neighbours(self, pixel):
        coloured_neighbours = dict()
        for neighbour_name, neighbour_colour in pixel.get_neighbours().items():
            if self.pixel_colour_feature.get_feature(neighbour_colour):
                coloured_neighbours.update({neighbour_name: neighbour_colour})
        return coloured_neighbours

class FeatureAsPercentageOfImage(ImageFeatureExtractor):
    def __init__(self, image_feature, null_pixel_value):
        ImageFeatureExtractor.__init__(self, null_pixel_value)
        self.image_feature = image_feature

    def get_feature(self, image):
        return len(self.image_feature.get_feature(image)) / self.get_number_of_pixels_in_image(image)

    def get_number_of_pixels_in_image(self, image):
        number_of_pixels = 0
        for column in image.get_pixels():
            number_of_pixels += len(column)
        return number_of_pixels