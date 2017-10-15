from sample.SampleSet import SampleSet

from ioer.LocationBuilder import LocationBuilder
from ioer.SampleOutputNameBuilder import SampleOutputNameBuilder
from ioer.SamplesIO import SamplesIO
from sample.Sample import Sample

class SampleSetIO(SamplesIO):
    def __init__(self, directory_separator = "/"):
        SamplesIO.__init__(self, directory_separator)

    def save_sample_sets_as_csv(self, sample_sets, student_number, save_location):
        for sample_set in sample_sets:
            self.save_sample_set_as_csv(sample_set, student_number, save_location)

    def save_sample_set_as_csv(self, sample_set, student_number, save_location):
        output_name_builder = SampleOutputNameBuilder(student_number, sample_set.sample_code, "-")
        output_location = LocationBuilder().build(save_location, sample_set.sample_code)
        self.write_samples_to_file_as_csv(output_name_builder, sample_set.samples, output_location)

    def get_all_sample_sets(self, sample_sets_to_get, samples_home_directory):
        sample_sets = []
        for sample_type in sample_sets_to_get:
            sample_images_of_type = self.get_samples_from_file(LocationBuilder().build(samples_home_directory, sample_type["location"]), "csv")
            samples_of_type = []
            for sample_image, sample_index in zip(sample_images_of_type, range(len(sample_images_of_type))):
                samples_of_type.append(Sample(sample_type["sample_code"], sample_index + 1, sample_image))
            sample_sets.append(SampleSet(sample_type["sample_code"], samples_of_type))
        return sample_sets

    def get_all_unprocessed_sample_sets(self, sample_sets_to_get, samples_home_directory):
        sample_sets = []
        for sample_type in sample_sets_to_get:
            sample_images_of_type = self.get_unprocessed_samples_from_file(LocationBuilder().build(samples_home_directory, sample_type["location"]), "csv")
            samples_of_type = []
            for sample_image, sample_index in zip(sample_images_of_type, range(len(sample_images_of_type))):
                samples_of_type.append(Sample(sample_type["sample_code"], sample_index + 1, sample_image))
            sample_sets.append(SampleSet(sample_type["sample_code"], samples_of_type))
        return sample_sets