from ioer.SampleSetIO import SampleSetIO
from ioer.IO import IO
from os import getcwd
from feature_extractor.features.neural_networks.NetworkTrainer import NESTrainer, AssignmentNeuralNetworkFitnessMetric, SymbolRecognitionNeuralNetworkBuilder
from random import sample

def convert_sample_sets_to_training_samples(sample_sets):
    training_samples = []
    for sample_set in sample_sets:
        for sample in sample_set.samples:
            training_samples.append([sample.sample_code, sample.get_pixel_vector()])
    return training_samples


home_directory = getcwd()
samples_sets_map = IO().open_json_file_as_map(home_directory, "processed_sample_sets.json")
sample_set_io = SampleSetIO()
sample_sets = sample_set_io.get_all_sample_sets(samples_sets_map["sample_types"], samples_sets_map["samples_location"])
training_samples = convert_sample_sets_to_training_samples(sample_sets)
training_samples = sample(training_samples, len(training_samples))

sample_types = []
for sample_type_dictionary in samples_sets_map["sample_types"]:
    sample_types.append(sample_type_dictionary["sample_code"])

network_trainer = NESTrainer((256, 16, 16, 16), (16, 16, 16, 12), AssignmentNeuralNetworkFitnessMetric(training_samples, sample_types))
weights = network_trainer.train(160)

hidden_layers_weights = weights[:-1]
hidden_layers_weights_json = []
for layer_index in range(len(hidden_layers_weights)):
    hidden_layers_weights_json.append(hidden_layers_weights[layer_index].tolist())

output_layer_weights = weights[-1]
output_layer_weights_json = output_layer_weights.tolist()

assignment_network_weights = dict({"symbol_recognition_network_weights" : {
    "hidden_layer_weights" : hidden_layers_weights_json,
    "output_layer_weights" : output_layer_weights_json
}})

IO().write_json_file(assignment_network_weights, home_directory, "symbol_recognition_network_weights.json")
print("done")
