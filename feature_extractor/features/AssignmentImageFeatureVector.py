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