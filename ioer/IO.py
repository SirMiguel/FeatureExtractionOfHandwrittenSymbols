from PIL import Image
from os import access, path, makedirs
import csv
import json

class IO:
    def __init__(self, directory_separator="/"):
        self.directory_separator = directory_separator

    def open_json_file_as_map(self, file_location, file_name):
        json_string = self.open_json_file(file_location, file_name)
        json_map = json.loads(json_string)
        return json_map

    def open_json_file(self, file_location, file_name):
        with open(file_location + self.directory_separator + file_name, "r") as file:
            json_string = file.read()
            file.close()
        return json_string

    def write_json_file(self, json_data, file_location, file_name):
        with self.get_file_to_write(file_name, file_location) as file:
            json.dump(json_data, file)
            #json_string = file.read()
         #   file.close()
        #return json_string

    def write_file(self, file, location, file_name):
        with self.get_file_to_write(file_name, location) as file:
            for line in file:
                file.write(line)
            file.close()

    def write_csv(self, csv_file, location, file_name):
        with self.get_file_to_write(file_name + ".csv", location) as file:
            csv_writer = csv.writer(file)
            for row in csv_file:
                csv_writer.writerow(row)
            file.close()

    def write_as_single_line_csv(self, csv_file, location, file_name):
        with self.get_file_to_write(file_name + ".csv", location) as file:
            csv_writer = csv.writer(file)
            #for row in csv_file:
            csv_writer.writerow(csv_file)
            file.close()

    def read_file(self, file_name, location):
        with self.get_file_to_read(file_name, location) as file:
            return file.read()

    def read_csv_as_list(self, file_name, location):
        with self.get_file_to_read(file_name, location) as csv_file:
            csv_reader =  csv.reader(csv_file)
            csv_array = []
            for row in csv_reader:
                csv_array.append([int(cell) for cell in row])
            return csv_array


    #def read_csv(self, ):

    def get_file_to_read(self, file_name, location):
        return open(self.get_file_path(file_name, location), "r")

    def get_file_to_write(self, file_name, location):
        self.create_directory(location)
        return open(self.get_file_path(file_name, location + "/"), "w")

    def get_file_path(self, file_name, location):
        return location + file_name

    def read_image(self, file_name, location):
        opened_image = Image.open(location + file_name)
        return opened_image

    def can_access_file(self, filename, location):
        return access(self.get_file_path(filename, location), 0)

    def create_directory(self, save_location):
        if not path.exists(save_location):
            makedirs(save_location)