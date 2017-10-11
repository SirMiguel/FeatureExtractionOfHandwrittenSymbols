import json
from ioer.IO import IO
from feature_extractor.image.Image import Image
from pandas import DataFrame
from feature_extractor.features.ImageFeatureExtractor import ColouredPixelsExtractor,ColouredPixelsWithColouredNamedNeighboursExtractor, ColouredPixelsWithAtMostColouredNeighbours, ColouredPixelsWithExactlyAsManyColouredNeighbours, ColouredPixelsWithAtLeastAsManyColouredNeighbours, ColouredPixelsWithNoNamedColouredNeighbours, ORComplexImageFeature, RowsWithAtLeastQuantityOfColourPixelsFeatureExtractor, ColumnsWithAtLeastQuantityOfColourPixelsFeatureExtractor, ConnectedColourRegionsInImage, FeatureAsPercentageOfImage, MinusSumComplexImageFeature, NeuralNetworkFeature
from feature_extractor.features.neural_networks.NeuralNetwork import AssignmentNeuralNetworkWithWeighsBuilder, AssignmentNeuralNetwork, NewAssignmentNeuralNetworkBuilder
from feature_extractor.features.neural_networks.Trainer import Trainer, TrainerFitnessMetric
from feature_extractor.image.Pixel import BlackPixel, WhitePixel

from numpy.random import randn

def open_json_file(file_location, file_name, directory_separator = "/"):
    with open(file_location + directory_separator + file_name, "r") as file:
        json_string = file.read()
        file.close()
    return json_string

def open_json_file_as_map(file_location, file_name):
    json_string = open_json_file(file_location, file_name)
    json_map = json.loads(json_string)
    return json_map

def get_thing(network_weights):
    sample_types = [1, 2, 3, 4, 5, 6, 7, 8, 9, 100, 200, 300]
    hidden_weights = []
    for layer_weights in network_weights[:-1]:
        hidden_weights.append(layer_weights)

    output_layer_data = dict()
    for sample_type, neuron_weight in zip(sample_types, network_weights[:-1]):
        output_layer_data.update({sample_type: neuron_weight})

    return AssignmentNeuralNetworkWithWeighsBuilder(network_weights, output_layer_data).build()


image_array = IO().read_csv_as_list("40153628-100-10.csv", "/Users/Michael/Documents/Computer Science/Third Year/AI & Data Analytics - CSC3060/Assignment_1/Data Set/Processed Samples/100/")
image_array_2 = IO().read_csv_as_list("40153628-100-1.csv", "/Users/Michael/Documents/Computer Science/Third Year/AI & Data Analytics - CSC3060/Assignment_1/Data Set/Processed Samples/100/")
image_array_3 = IO().read_csv_as_list("40153628-100-2.csv", "/Users/Michael/Documents/Computer Science/Third Year/AI & Data Analytics - CSC3060/Assignment_1/Data Set/Processed Samples/100/")

image_array_4 = IO().read_csv_as_list("40153628-1-1.csv", "/Users/Michael/Documents/Computer Science/Third Year/AI & Data Analytics - CSC3060/Assignment_1/Data Set/Processed Samples/1/")


image = Image(image_array, 16, 16)
image2 = Image(image_array_2, 16, 16)
image3 = Image(image_array_3, 16, 16)
image4 = Image(image_array_4, 16, 16)

print(DataFrame(image.pixels))

#for row_index in range(image.height):
 #   for column_index in range(image.width):
  #      print("Nighbours of pixel ", column_index, ", ", row_index, " : ", PixelNeighbours(0).get_feature(image, column_index, row_index))

#print("number of black pixels", len(ColouredPixels(1).get_feature(image)))
black_colour = BlackPixel()
white_colour = WhitePixel()

sample_types = [1, 2, 3, 4, 5, 6, 7, 8, 9, 100, 200, 300]






sample_set = [[100, image.get_pixel_vector()]]
sample_set.append([100, image2.get_pixel_vector()])
sample_set.append([100, image3.get_pixel_vector()])
sample_set.append([1, image4.get_pixel_vector()])


netwokr_trainer = Trainer((256, 16, 16), (16, 16, 12), TrainerFitnessMetric(sample_set))
weights = netwokr_trainer.train(10)

sample_types = [1, 2, 3, 4, 5, 6, 7, 8, 9, 100, 200, 300]
hidden_weights = []
for layer_weights in weights[:-1]:
    hidden_weights.append(layer_weights)

output_layer_data = dict()
output_weights = weights[-1]
for sample_type, neuron_weight in zip(sample_types, output_weights):
     output_layer_data.update({sample_type: neuron_weight})

network = AssignmentNeuralNetworkWithWeighsBuilder(hidden_weights, output_layer_data).build()

output_nodes_data = dict()
output_weights = weights[:-1]
for weight, sample_type in zip(output_weights, sample_types):
    output_nodes_data.update({sample_type : weight})

#neural_network = AssignmentNeuralNetworkWithWeighsBuilder(weights[:-1], output_nodes_data).build()

feature_one = NeuralNetworkFeature(network, white_colour.get_colour())

print("1. Actual symbol in image.", feature_one.get_feature(image))


print("2. Number of black pixels in the image.", len(ColouredPixelsExtractor(black_colour.get_colour(), white_colour.get_colour()).get_feature(image)))
#print("black pixels with black neighbours", len(ColouredPixelsColouredNeighboursExtractor(black_colour.get_colour(), black_colour.get_colour(), white_colour.get_colour()).get_feature(image)))

colour_matching_neighbours = ["right", "left", "upper", "lower"]
print("3. Number of black pixels with black pixel neighbours at", colour_matching_neighbours, len(ColouredPixelsWithColouredNamedNeighboursExtractor(black_colour.get_colour(), black_colour.get_colour(), colour_matching_neighbours, white_colour.get_colour()).get_feature(image)))
print("4. Number of black pixels with at most 3 black pixel neighbours.", len(ColouredPixelsWithAtMostColouredNeighbours(black_colour.get_colour(), black_colour.get_colour(), 3, white_colour.get_colour()).get_feature(image)))
print("5. Number of black pixels with exactly 4 black pixel neighbours.", len(ColouredPixelsWithExactlyAsManyColouredNeighbours(black_colour.get_colour(), black_colour.get_colour(), 4, white_colour.get_colour()).get_feature(image)))
print("6. Number of black pixels with 5 or more black pixel neighbours.", len(ColouredPixelsWithAtLeastAsManyColouredNeighbours(black_colour.get_colour(), black_colour.get_colour(), 5, white_colour.get_colour()).get_feature(image)))
forbidden_colour_neighbours_one = ["right", "upper-right", "lower-right"]
feature_seven = ColouredPixelsWithNoNamedColouredNeighbours(black_colour.get_colour(), forbidden_colour_neighbours_one, black_colour.get_colour(), white_colour.get_colour())
print("7. Number of black pixels with NO black pixel neighbours at any of ", forbidden_colour_neighbours_one, len(feature_seven.get_feature(image)))


forbidden_colour_neighbours_two = ["left", "upper-left", "lower-left"]
feature_eight = ColouredPixelsWithNoNamedColouredNeighbours(black_colour.get_colour(), forbidden_colour_neighbours_two, black_colour.get_colour(), white_colour.get_colour())
print("8. Number of black pixels with NO black pixel neighbours at any of", forbidden_colour_neighbours_two, len(feature_eight.get_feature(image)))

forbidden_colour_neighbours_three = ["upper", "upper-left", "upper-right"]
feature_nine = ColouredPixelsWithNoNamedColouredNeighbours(black_colour.get_colour(),
                                                      forbidden_colour_neighbours_three,
                                                      black_colour.get_colour(),
                                                      white_colour.get_colour())
print("9. Number of black pixels with NO black pixel neighbours at any of",
      forbidden_colour_neighbours_three,
      len(feature_nine.get_feature(image)))

forbidden_colour_neighbours_four = ["lower", "lower-left", "lower-right"]
feature_ten = ColouredPixelsWithNoNamedColouredNeighbours(black_colour.get_colour(),
                                                      forbidden_colour_neighbours_four,
                                                      black_colour.get_colour(),
                                                      white_colour.get_colour())
print("10. Number of black pixels with NO black pixel neighbours at any of",
      forbidden_colour_neighbours_four,
      len(feature_ten.get_feature(image)))

feature_eleven = ORComplexImageFeature([feature_seven, feature_eight], white_colour.get_colour())
print("11. Number of black pixels (satisfying the condition of Rule 7) OR (satisfying the condition of Rule 8).", len(feature_eleven.get_feature(image)))


feature_twelve = ORComplexImageFeature([feature_nine, feature_ten], white_colour.get_colour())
print("12. Number of black pixels (satisfying the condition of Rule 9) OR (satisfying the condition of Rule 10).", len(feature_twelve.get_feature(image)))

feature_thirteen_colour_neighbours_excluded = ["right", "lower-right", "lower"]
feature_thirteen = ColouredPixelsWithNoNamedColouredNeighbours(black_colour.get_colour(), feature_thirteen_colour_neighbours_excluded, black_colour.get_colour(), white_colour.get_colour())
print("13. Number of black pixels with NO black pixel neighbours at any of", feature_thirteen_colour_neighbours_excluded, len(feature_thirteen.get_feature(image)))

feature_fourteen_colour_neighbours_excluded = ["upper", "upper-left", "left"]
feature_fourteen = ColouredPixelsWithNoNamedColouredNeighbours(black_colour.get_colour(), feature_fourteen_colour_neighbours_excluded, black_colour.get_colour(), white_colour.get_colour())
print("14. Number of black pixels with NO black pixel neighbours at any of", feature_fourteen_colour_neighbours_excluded, len(feature_fourteen.get_feature(image)))

feature_fifteen_colour_neighbours_excluded = ["upper", "upper-right", "right"]
feature_fifteen = ColouredPixelsWithNoNamedColouredNeighbours(black_colour.get_colour(), feature_fifteen_colour_neighbours_excluded, black_colour.get_colour(), white_colour.get_colour())
print("15. Number of black pixels with NO black pixel neighbours at any of", feature_fifteen_colour_neighbours_excluded,len(feature_fifteen.get_feature(image)))

feature_sixteen_colour_neighbours_excluded = ["left", "lower-left", "lower"]
feature_sixteen = ColouredPixelsWithNoNamedColouredNeighbours(black_colour.get_colour(), feature_sixteen_colour_neighbours_excluded, black_colour.get_colour(), white_colour.get_colour())
print("16. Number of black pixels with NO black pixel neighbours at any of", feature_sixteen_colour_neighbours_excluded, len(feature_sixteen.get_feature(image)))

feature_seventeen = ORComplexImageFeature([feature_thirteen, feature_fourteen], white_colour.get_colour())
print("17. Number of black pixels (satisfying the condition of Rule 13) OR (satisfying the condition of Rule 14).", len(feature_seventeen.get_feature(image)))


feature_eighteen = ORComplexImageFeature([feature_fifteen, feature_sixteen], white_colour.get_colour())
print("18. Number of black pixels (satisfying the condition of Rule 15) OR (satisfying the condition of Rule 16).", len(feature_eighteen.get_feature(image)))

feature_nineteen = ORComplexImageFeature([feature_eleven, feature_twelve], white_colour.get_colour())
print("19. Number of black pixels (satisfying the condition of Rule 11) OR (satisfying the condition of Rule 12).", len(feature_nineteen.get_feature(image)))

feature_twenty = ORComplexImageFeature([feature_seventeen, feature_eighteen], white_colour.get_colour())
print("20. Number of black pixels (satisfying the condition of Rule 17) OR (satisfying the condition of Rule 18).", len(feature_twenty.get_feature(image)))

feature_twenty_one = RowsWithAtLeastQuantityOfColourPixelsFeatureExtractor(1, black_colour.get_colour(), white_colour.get_colour())
print("21. Number of rows with at least one black pixel.", len(feature_twenty_one.get_feature(image)))

feature_twenty_two = ColumnsWithAtLeastQuantityOfColourPixelsFeatureExtractor(1, black_colour.get_colour(), white_colour.get_colour())
print("22. Number of columns with at least one black pixel.", len(feature_twenty_two.get_feature(image)))

feature_twenty_three = RowsWithAtLeastQuantityOfColourPixelsFeatureExtractor(5, black_colour.get_colour(), white_colour.get_colour())
print("23. Number of rows with at least five black pixels.", len(feature_twenty_three.get_feature(image)))

feature_twenty_four = ColumnsWithAtLeastQuantityOfColourPixelsFeatureExtractor(5, black_colour.get_colour(), white_colour.get_colour())
print("24. Number of columns with at least five black pixels.", len(feature_twenty_four.get_feature(image)))

feature_twenty_five = ConnectedColourRegionsInImage(black_colour.get_colour(), white_colour.get_colour())
print("""25. Two black pixels A and B are connected if they are neighbours of each other, or if a black
        pixel neighbour of A is connected to B (this definition is actually symmetric); a connected
        region is a set of black pixels which are connected to each other; this feature has the number
        of connected regions in the image""", len(feature_twenty_five.get_feature(image)))

feature_twenty_six = FeatureAsPercentageOfImage(ColouredPixelsWithAtMostColouredNeighbours(black_colour.get_colour(), black_colour.get_colour(), 3, white_colour.get_colour()), white_colour.get_colour())
print("26. Percentage of black pixels with at most 3 black pixel neighbours.", feature_twenty_six.get_feature(image))

feature_twenty_seven = FeatureAsPercentageOfImage(ColouredPixelsWithExactlyAsManyColouredNeighbours(black_colour.get_colour(), black_colour.get_colour(), 4, white_colour.get_colour()), white_colour.get_colour())
print("27. Percentage of black pixels with exactly 4 black pixel neighbours.", feature_twenty_seven.get_feature(image))

feature_twenty_eight = FeatureAsPercentageOfImage(ColouredPixelsWithAtLeastAsManyColouredNeighbours(black_colour.get_colour(), black_colour.get_colour(), 5, white_colour.get_colour()), white_colour.get_colour())
print("28. Percentage of black pixels with 5 or more black pixel neighbours.", feature_twenty_eight.get_feature(image))


feature_twenty_nine = MinusSumComplexImageFeature([RowsWithAtLeastQuantityOfColourPixelsFeatureExtractor(5, black_colour.get_colour(), white_colour.get_colour()), ColumnsWithAtLeastQuantityOfColourPixelsFeatureExtractor(5, black_colour.get_colour(), white_colour.get_colour())], white_colour.get_colour())
print("29. (Number of rows with at least five black pixels) minus (number of columns with at least five black pixels).", (feature_twenty_nine.get_feature(image)))

#print("number of black pixels with right, left, upper, and lower black neighbours", ColouredPixelsColouredNeighbours(black_colour, black_colour, white_colour).get_feature(image))
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
