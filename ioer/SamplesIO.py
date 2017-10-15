import os
import re

from ioer.IO import IO

class SamplesIO(IO):
    def __init__(self, directory_separator = "/"):
        IO.__init__(self, directory_separator)

    def get_samples_from_file(self, samples_location, sample_file_extension):
        samples = []
        for filename in os.listdir(samples_location):
            if self.can_access_file(filename, samples_location) and self.is_file(filename, sample_file_extension):
                samples.append(IO.read_csv_as_list(self, filename, samples_location))
        return samples

    def get_unprocessed_samples_from_file(self, samples_location, sample_file_extension):
        samples = []
        for filename in os.listdir(samples_location):
            if self.can_access_file(filename, samples_location) and self.is_file(filename, sample_file_extension):
                samples.append(IO.read_image(self, filename, samples_location))
        return samples

    def write_samples_to_file_as_csv(self, output_name_builder, samples, save_location):
        self.create_directory(save_location)
        for sample in samples:
            IO.write_csv(self, sample.sample_image,
                         save_location,
                         output_name_builder.build(sample.sample_number))

    def get_full_filename_of_sample(self, sample, pre_appended_name = "", separator = ""):
        return pre_appended_name + separator + sample.get_sample_fullname(separator)

    def is_file(self, filename, file_extension):
        return re.match(".+[." + file_extension + "]", filename)