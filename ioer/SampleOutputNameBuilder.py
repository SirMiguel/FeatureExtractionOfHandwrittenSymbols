
class SampleOutputNameBuilder:
    def __init__(self, student_number, sample_code, separator = "-",):
        self.student_number = student_number
        self.sample_code = sample_code
        self.separator = separator

    def build(self, sample_number):
        return (str(self.student_number) + self.separator + str(self.sample_code) +
                self.separator + str(sample_number))