from ioer.IO import IO
from ioer.SampleSetIO import SampleSetIO
from feature_extractor.features.AssignmentImageFeatureVector import AssignmentImageFeatureVectorBuilder
from feature_extractor.image.Pixel import BlackPixel, WhitePixel
from feature_extractor.features.neural_networks.NeuralNetwork import SymbolRecognitionNeuralNetworkBuilder
from os import getcwd
from feature_extractor.image.Image import Image
from ioer.SampleOutputNameBuilder import SampleOutputNameBuilder
from ioer.LocationBuilder import LocationBuilder
#open all sample sets
#open network weights
#create neural network
#get output layer dict keys

home_directory = getcwd()
samples_sets_data_map = IO().open_json_file_as_map(home_directory, "processed_sample_sets.json")
sample_set_io = SampleSetIO()
io = IO()

sample_sets = sample_set_io.get_all_sample_sets(samples_sets_data_map["sample_types"], samples_sets_data_map["samples_location"])

#get network
network_weights = io.open_json_file_as_map(home_directory, "symbol_recognition_network_weights.json")["symbol_recognition_network_weights"]
hidden_layer_weights = network_weights["hidden_layer_weights"]
output_layer_weights = network_weights["output_layer_weights"]
sample_types = []
for sample_type_dictionary in samples_sets_data_map["sample_types"]:
    sample_types.append(sample_type_dictionary["sample_code"])
symbol_recognition_network = SymbolRecognitionNeuralNetworkBuilder(hidden_layer_weights, output_layer_weights, sample_types).build()

white_colour = WhitePixel().get_colour()
black_colour = BlackPixel().get_colour()
assignment_image_feature_vector = AssignmentImageFeatureVectorBuilder(symbol_recognition_network,
                                                                      black_colour,
                                                                      white_colour,
                                                                      white_colour).build()
features_output_location = LocationBuilder().build(home_directory, "features")
for sample_set in sample_sets:
    sample_set_assignment_feature_vector = []
    for sample in sample_set.samples:
        image_feature_vector = assignment_image_feature_vector.get_feature_vector(Image(sample.sample_image, len(sample.sample_image), len(sample.sample_image[0])))
        print(image_feature_vector)
        io.write_as_single_line_csv(image_feature_vector, LocationBuilder().build(features_output_location, sample.sample_code), SampleOutputNameBuilder(40153628, sample.sample_code).build(sample.sample_number, "features"))

#for each sample set
    #for each image
        #get image feature vector
        #save image feature vector
    #get the median value of each feature for all samples in the set
    #get the mean of each feature for all samples in the set
    #save mean and median feature vectors



