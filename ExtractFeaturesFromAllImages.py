import json
from ioer.IO import IO
from numpy import array
from feature_extractor.image.Image import Image
from feature_extractor.features.PixelNeighbour import Neighbour
from pandas import DataFrame

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

for row_index in range(image.height):
    for column_index in range(image.width):
        print("Nighbours of pixel ", column_index, ", ", row_index, " : ", Neighbour(0).get_neighbours(image, column_index, row_index))


