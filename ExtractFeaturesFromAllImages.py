import json
from ioer.IO import IO
from feature_extractor.image.Image import Image
from pandas import DataFrame
from feature_extractor.features.ImageFeatureExtractor import ColouredPixelsExtractor, ColouredPixelsColouredNeighboursExtractor
from feature_extractor.image.Pixel import BlackPixel, WhitePixel


def open_json_file(file_location, file_name, directory_separator = "/"):
    with open(file_location + directory_separator + file_name, "r") as file:
        json_string = file.read()
        file.close()
    return json_string

def open_json_file_as_map(file_location, file_name):
    json_string = open_json_file(file_location, file_name)
    json_map = json.loads(json_string)
    return json_map


image_array = IO().read_csv_as_list("40153628-100-1.csv", "/Users/Michael/Documents/Computer Science/Third Year/AI & Data Analytics - CSC3060/Assignment_1/Data Set/Processed Samples/100/")
image = Image(image_array, 16, 16)
print(DataFrame(image.pixels))

#for row_index in range(image.height):
 #   for column_index in range(image.width):
  #      print("Nighbours of pixel ", column_index, ", ", row_index, " : ", PixelNeighbours(0).get_feature(image, column_index, row_index))

#print("number of black pixels", len(ColouredPixels(1).get_feature(image)))
black_colour = BlackPixel()
white_colour = WhitePixel()
print("number of black pixels", ColouredPixelsExtractor(black_colour.get_colour()).get_feature(image))
print("black pixels with black neighbours", ColouredPixelsColouredNeighboursExtractor(black_colour.get_colour(), white_colour.get_colour()).get_feature(image))

#print("number of black pixels with right, left, upper, and lower black neighbours", ColouredPixelsColouredNeighbours(black_colour, black_colour, white_colour).get_feature(image))
# neighbours_to_get = ["right", "left", "upper", "lower"]
#
# image_pixels_with_black_pixel_neighbours = ColouredPixelsWithColouredNeighbours(0, 1, 1).get_feature(image)
# black_pixels_with_neighbours = []
#
# for neighbours in image_pixels_with_black_pixel_neighbours:
#     match = True
#     for neighbour in neighbours_to_get:
#         if neighbour not in neighbours:
#             match = False
#
#     if match:
#         black_pixels_with_neighbours.append(neighbours)
#
# at_most_black_neighbours = []
# for neighbours in image_pixels_with_black_pixel_neighbours:
#     if len(neighbours) <= 3:
#         at_most_black_neighbours.append(neighbours)
#
# print("number of black pixels with right left upper lower neighbours", len(black_pixels_with_neighbours))
# print("number of black pixels with at most 3 black neighbours", len(at_most_black_neighbours))
