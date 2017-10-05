
class LocationBuilder:
    def __init__(self, directory_separator = "/"):
        self.directory_separator = directory_separator

    def build(self, *args):
        full_directory = ""
        for sub_directory in args:
            full_directory += sub_directory + self.directory_separator
        return full_directory