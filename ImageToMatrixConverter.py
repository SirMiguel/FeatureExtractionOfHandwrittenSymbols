# from tkinter import PhotoImage, Tk
#two parts:
    #one: pass each image into the other script and then save it
    #two: convert a given BW image into a

#where to get images
#where to save csv matrixes

#open each image
#for

#Screw that



#convert PNM BW Image to CSV Binary Matrix
# 1 is black, 0 is white

# Boundary value is given
# Image is given
# Output file name is given

# Create a matrix of the same dimensions at the image given

# For each column
    # For each row
        # Look at value of pixel:
        # If the pixel is above the boundary:
            # Give it a one
        # Else:
            # Give it a zero

# Save the matrix as a CSV file
'''
class ListToMatrix:
    def __init__(self):
        pass

    def get_matrix_from_list(self, pixel_list, break_point):
        number_of_rows = self.get_number_of_rows(len(pixel_list), break_point)
        last_row_index = number_of_rows - 1
        matrix = [[pixel_list[cell + column] for cell in range(last_row_index)] for column in range(number_of_rows)]
        return matrix

    def get_number_of_rows(self, length_of_list, break_point):
        return int(length_of_list / break_point)
'''
'''
class ImageToMatrix:
    def __init__(self):
        pass

    def get_matrix_from_image(self, image):
        last_column, last_row = image.width, image.height
        matrix = []
        for column in range(last_column):
            matrix.append([image.getpixel((column, cell)) for cell in range(last_row)])
        return matrix
'''
class Binary_Arbitrater:
    def __init__(self, boundary):
        self.boundary = boundary

    def get_binary_from_value(self, value):
        return 0 if value > self.boundary else 1

class ImageToBinaryMatrixConverter:
    def __init__(self, binary_arbitrater):
        self.binary_arbitrater = binary_arbitrater

    def convert_image_matrix_to_binary_matrix(self, image_pixels):
        binary_matrix = []
        for column in image_pixels:
             binary_matrix.append([self.pixel_to_binary(cell) for cell in column])
        return binary_matrix

    def pixel_to_binary(self, pixel):
        return self.binary_arbitrater.get_binary_from_value(pixel)
