from feature_extractor.features.ImageFeature import * 

class AssignmentImageFeatureVectorBuilder:

    def __init__(self, symbol_recognition_network, black_pixel_colour, white_pixel_colour, null_pixel_colour):
        #Please note: Feature vector is 0 indexed here when referring to other features
        self.symbol_recognition_network = symbol_recognition_network
        self.black_pixel_colour = black_pixel_colour
        self.white_pixel_colour = white_pixel_colour
        self.null_pixel_colour = null_pixel_colour
        
    def build(self):
        assignment_features = []

        assignment_features.append(NeuralNetworkFeature(self.symbol_recognition_network, self.null_pixel_colour))

        assignment_features.append(ColouredPixels(self.black_pixel_colour, self.null_pixel_colour))

        feature_three_neighbours = ["right", "left", "upper", "lower"]
        assignment_features.append(ColouredPixelsWithColouredNamedNeighbours(self.black_pixel_colour, self.black_pixel_colour,
                                                                             feature_three_neighbours,
                                                                             self.white_pixel_colour))

        assignment_features.append(ColouredPixelsWithAtMostColouredNeighbours(self.black_pixel_colour, self.black_pixel_colour,
                                                                              3, self.white_pixel_colour))

        assignment_features.append(ColouredPixelsWithExactlyAsManyColouredNeighbours(self.black_pixel_colour,
                                                                                     self.black_pixel_colour, 4,
                                                                                     self.white_pixel_colour))

        assignment_features.append(ColouredPixelsWithAtLeastAsManyColouredNeighbours(self.black_pixel_colour,
                                                                                     self.black_pixel_colour, 5,
                                                                                     self.white_pixel_colour))

        feature_seven_neighbours = ["right", "upper-right", "lower-right"]
        assignment_features.append(ColouredPixelsWithNoNamedColouredNeighbours(self.black_pixel_colour,
                                                                               feature_seven_neighbours,
                                                                               self.black_pixel_colour,
                                                                               self.white_pixel_colour))

        feature_eight_neighbours = ["left", "upper-left", "lower-left"]
        assignment_features.append(ColouredPixelsWithNoNamedColouredNeighbours(self.black_pixel_colour,
                                                                               feature_eight_neighbours,
                                                                               self.black_pixel_colour,
                                                                               self.white_pixel_colour))

        feature_nine_neighbours = ["upper", "upper-left", "upper-right"]
        assignment_features.append(ColouredPixelsWithNoNamedColouredNeighbours(self.black_pixel_colour,
                                                                               feature_nine_neighbours,
                                                                               self.black_pixel_colour,
                                                                               self.white_pixel_colour))

        forbidden_colour_neighbours_four = ["lower", "lower-left", "lower-right"]
        assignment_features.append(ColouredPixelsWithNoNamedColouredNeighbours(self.black_pixel_colour,
                                                                               forbidden_colour_neighbours_four,
                                                                               self.black_pixel_colour,
                                                                               self.null_pixel_colour))

        assignment_features.append(ORComplexImageFeature([assignment_features[6], assignment_features[7]],
                                                         self.null_pixel_colour))

        assignment_features.append(
            ORComplexImageFeature([assignment_features[8], assignment_features[9]], self.null_pixel_colour))

        feature_thirteen_neighbours = ["right", "lower-right", "lower"]
        assignment_features.append(ColouredPixelsWithNoNamedColouredNeighbours(self.black_pixel_colour,
                                                                               feature_thirteen_neighbours,
                                                                               self.black_pixel_colour,
                                                                               self.null_pixel_colour))

        feature_fourteen_neighbours = ["upper", "upper-left", "left"]
        assignment_features.append(ColouredPixelsWithNoNamedColouredNeighbours(self.black_pixel_colour,
                                                                               feature_fourteen_neighbours,
                                                                               self.black_pixel_colour,
                                                                               self.null_pixel_colour))

        feature_fifteen_neighbours = ["upper", "upper-right", "right"]
        assignment_features.append(ColouredPixelsWithNoNamedColouredNeighbours(self.black_pixel_colour,
                                                                               feature_fifteen_neighbours,
                                                                               self.black_pixel_colour,
                                                                               self.null_pixel_colour))

        feature_sixteen_neighbours = ["left", "lower-left", "lower"]
        assignment_features.append(ColouredPixelsWithNoNamedColouredNeighbours(self.black_pixel_colour,
                                                                               feature_sixteen_neighbours,
                                                                               self.black_pixel_colour,
                                                                               self.null_pixel_colour))

        assignment_features.append(
            ORComplexImageFeature([assignment_features[12], assignment_features[13]], self.null_pixel_colour))

        assignment_features.append(
            ORComplexImageFeature([assignment_features[14], assignment_features[15]], self.null_pixel_colour))

        assignment_features.append(
            ORComplexImageFeature([assignment_features[10], assignment_features[11]], self.null_pixel_colour))

        assignment_features.append(
            ORComplexImageFeature([assignment_features[16], assignment_features[17]], self.null_pixel_colour))

        assignment_features.append(RowsWithAtLeastQuantityOfColourPixelsFeature(1, self.black_pixel_colour,
                                                                                self.null_pixel_colour))

        assignment_features.append(ColumnsWithAtLeastQuantityOfColourPixelsFeature(1, self.black_pixel_colour,
                                                                                   self.null_pixel_colour))

        assignment_features.append(RowsWithAtLeastQuantityOfColourPixelsFeature(5, self.black_pixel_colour,
                                                                                self.null_pixel_colour))

        assignment_features.append(ColumnsWithAtLeastQuantityOfColourPixelsFeature(5, self.black_pixel_colour,
                                                                                   self.null_pixel_colour))

        assignment_features.append(ConnectedColourRegionsInImage(self.black_pixel_colour, self.null_pixel_colour))

        assignment_features.append(FeatureAsPercentageOfImage(
            ColouredPixelsWithAtMostColouredNeighbours(self.black_pixel_colour, self.black_pixel_colour, 3,
                                                       self.white_pixel_colour), self.null_pixel_colour))

        assignment_features.append(FeatureAsPercentageOfImage(
            ColouredPixelsWithExactlyAsManyColouredNeighbours(self.black_pixel_colour, self.black_pixel_colour, 4,
                                                              self.white_pixel_colour), self.null_pixel_colour))

        assignment_features.append(FeatureAsPercentageOfImage(
            ColouredPixelsWithAtLeastAsManyColouredNeighbours(self.black_pixel_colour, self.black_pixel_colour, 5,
                                                              self.white_pixel_colour), self.null_pixel_colour))

        assignment_features.append(MinusSumComplexImageFeature(
            [RowsWithAtLeastQuantityOfColourPixelsFeature(5, self.black_pixel_colour, self.white_pixel_colour),
             ColumnsWithAtLeastQuantityOfColourPixelsFeature(5, self.black_pixel_colour, self.null_pixel_colour)],
            self.white_pixel_colour))

        assignment_features.append(ConnectedColourRegionsInImage(self.white_pixel_colour, self.black_pixel_colour))  # todo check
        return AssignmentImageFeatureVector(assignment_features)

#
# #         print("1. Actual symbol in image.", feature_one.get_feature(image))
# #         print("2. Number of black pixels in the image.", len(feature_two.get_feature(image)))
# #   print("3. Number of black pixels with black pixel neighbours at", colour_matching_neighbours,
# #              len(feature_three.get_feature(image)))
# #         print("4. Number of black pixels with at most 3 black pixel neighbours.", len(feature_four.get_feature(image)))
# #        print("5. Number of black pixels with exactly 4 black pixel neighbours.", len(feature_five.get_feature(image)))
# #        print("6. Number of black pixels with 5 or more black pixel neighbours.", len(feature_six.get_feature(image)))
# # print("7. Number of black pixels with NO black pixel neighbours at any of ", forbidden_colour_neighbours_one,
# #        print("8. Number of black pixels with NO black pixel neighbours at any of", forbidden_colour_neighbours_two,
# # print("9. Number of black pixels with NO black pixel neighbours at any of",
# #              forbidden_colour_neighbours_three,
# #              len(feature_nine.get_feature(image)))
#  print("10. Number of black pixels with NO black pixel neighbours at any of",
#               forbidden_colour_neighbours_four,
#               len(feature_ten.get_feature(image)))
# print(
#             "11. Number of black pixels (satisfying the condition of Rule 7) OR (satisfying the condition of Rule 8).",
#             len(feature_eleven.get_feature(image)))
# print(
#     "12. Number of black pixels (satisfying the condition of Rule 9) OR (satisfying the condition of Rule 10).",
#     len(feature_twelve.get_feature(image)))
# print("13. Number of black pixels with NO black pixel neighbours at any of",
#               feature_thirteen_colour_neighbours_excluded, len(feature_thirteen.get_feature(image)))
# print("14. Number of black pixels with NO black pixel neighbours at any of",
#       feature_fourteen_colour_neighbours_excluded, len(feature_fourteen.get_feature(image)))
# print("15. Number of black pixels with NO black pixel neighbours at any of",
#       feature_fifteen_colour_neighbours_excluded, len(feature_fifteen.get_feature(image)))
# print("16. Number of black pixels with NO black pixel neighbours at any of",
#       feature_sixteen_colour_neighbours_excluded, len(feature_sixteen.get_feature(image)))
# print(
#             "17. Number of black pixels (satisfying the condition of Rule 13) OR (satisfying the condition of Rule 14).",
#             len(feature_seventeen.get_feature(image)))
# print(
#             "18. Number of black pixels (satisfying the condition of Rule 15) OR (satisfying the condition of Rule 16).",
#             len(feature_eighteen.get_feature(image)))
# print(
#             "19. Number of black pixels (satisfying the condition of Rule 11) OR (satisfying the condition of Rule 12).",
#             len(feature_nineteen.get_feature(image)))
# print(
#     "20. Number of black pixels (satisfying the condition of Rule 17) OR (satisfying the condition of Rule 18).",
#     len(feature_twenty.get_feature(image)))
# print("21. Number of rows with at least one black pixel.", len(feature_twenty_one.get_feature(image)))
# print("22. Number of columns with at least one black pixel.", len(feature_twenty_two.get_feature(image)))
# print("23. Number of rows with at least five black pixels.", len(feature_twenty_three.get_feature(image)))
# print("24. Number of columns with at least five black pixels.", len(feature_twenty_four.get_feature(image)))
# print("""25. Two black pixels A and B are connected if they are neighbours of each other, or if a black
#                pixel neighbour of A is connected to B (this definition is actually symmetric); a connected
#                region is a set of black pixels which are connected to each other; this feature has the number
#                of connected regions in the image""", len(feature_twenty_five.get_feature(image)))
# print("26. Percentage of black pixels with at most 3 black pixel neighbours.",
#       feature_twenty_six.get_feature(image))
# print("27. Percentage of black pixels with exactly 4 black pixel neighbours.",
#               feature_twenty_seven.get_feature(image))
# print("28. Percentage of black pixels with 5 or more black pixel neighbours.",
#               feature_twenty_eight.get_feature(image))
# print(
#             "29. (Number of rows with at least five black pixels) minus (number of columns with at least five black pixels).",
#             (feature_twenty_nine.get_feature(image)))
# print(
#             "30. The number of background areas in the image. A background area is defined as an area of only white pixels. This is useful for detecting areas of loops/rings in an image"
#             ", as the interior of the ring will be an area of background colour",

class AssignmentImageFeatureVector:

    def __init__(self, image_features):
        self.image_features = image_features

    def get_feature_vector(self, image):
        image_feature_vector = []
        for image_feature in self.image_features:
            image_feature = image_feature.get_feature(image)
            if isinstance(image_feature, list) or isinstance(image_feature, dict):
                image_feature_vector.append(len(image_feature))
            else:
                image_feature_vector.append(image_feature)
        return image_feature_vector