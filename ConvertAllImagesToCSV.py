import json
from sample.SampleSet import SampleSet
from numpy import array
from ImageToMatrixConverter import ImageToBinaryMatrixConverter, Binary_Arbitrater
from ioer.SampleSetIO import SampleSetIO
from sample.Sample import Sample
from os import getcwd


def open_json_file(file_location, file_name, directory_separator = "/"):
    with open(file_location + directory_separator + file_name, "r") as file:
        json_string = file.read()
        file.close()
    return json_string

def open_json_file_as_map(file_location, file_name):
    json_string = open_json_file(file_location, file_name)
    json_map = json.loads(json_string)
    return json_map


def get_processed_sample(sample, image_to_binary_matrix_converter):
    return Sample(sample.sample_code, sample.sample_number,
                  image_to_binary_matrix_converter.convert_image_matrix_to_binary_matrix(array(sample.sample_image)))

def convert_all_sets_to_binary_matrices(sample_sets):
    converted_sample_sets = []
    for sample_set in sample_sets:
        converted_sample_set = []
        for sample in sample_set.samples:
            converted_sample_set.append(get_processed_sample(sample, image_to_binary_matrix_converter))
        converted_sample_sets.append(SampleSet(sample_set.sample_code, converted_sample_set))
    return converted_sample_sets

    #do the thing about getting files and saving them
home_directory = getcwd()#"/Users/Michael/Documents/Computer Science/Third Year/AI & Data Analytics - CSC3060/Assignment_1"
unprocessed_sample_data_map = open_json_file_as_map(home_directory, "unprocessed_sample_data.json")

sample_types = unprocessed_sample_data_map["sample_types"]
unprocessed_samples_location = unprocessed_sample_data_map["samples_location"]
unprocessed_samples_file_type = unprocessed_sample_data_map["file_type"]

sample_set_io = SampleSetIO()

# Get all images that need to be converted
unprocessed_sample_sets = sample_set_io.get_all_unprocessed_sample_sets(sample_types,
                                                            unprocessed_samples_location)

#convert each sample in type to a binary matrix
binary_arbitrator_boundary = unprocessed_sample_data_map["binary_arbitrator_boundary"]
image_to_binary_matrix_converter = ImageToBinaryMatrixConverter(Binary_Arbitrater(binary_arbitrator_boundary))
processed_sample_sets = convert_all_sets_to_binary_matrices(unprocessed_sample_sets)

#save all files
output_data_attributes_map = open_json_file_as_map(home_directory, "processed_sample_output_data.json")
student_number = output_data_attributes_map["student_number"]
save_location = output_data_attributes_map["samples_location"]
SampleSetIO().save_sample_sets_as_csv(processed_sample_sets, student_number, save_location)
