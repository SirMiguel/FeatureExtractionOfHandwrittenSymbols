from numpy import dot

class ActivationFunction:
    def __init__(self):
        pass

    def get_response(self, input):
        raise NotImplementedError("Activation Function has no default implementation,"
                                  "you must derive a class from it")

    def get_derivative(self, input):
        raise NotImplementedError("Activation Function has no default implementation,"
                                  "you must derive a class from it")

class RectifiedLinearUnit(ActivationFunction):
    def __init__(self):
        ActivationFunction.__init__(self)

    def get_response(self, input):
        return  max([0, input])

    def get_derivative(self, input):
        return 1 if input > 0 else 0

class ClassifierRELU(RectifiedLinearUnit):
    def __init__(self, class_of_unit):
        RectifiedLinearUnit.__init__(self)
        self.class_of_unit = class_of_unit

    def get_response(self, input):
        return dict({self.class_of_unit : RectifiedLinearUnit.get_response(self, input)})

class Neuron:
    def __init__(self, weight_vector, activation_function):
        self.weights = weight_vector
        self.activation_function = activation_function

    def think(self, input_vector):
        return self.activation_function.get_response(self.get_weighted_input(input_vector))

    def get_derivative(self, input):
        return self.activation_function.get_derivative(self.get_weighted_input(input))

    def get_weighted_input(self, input_vector):
        dot_prod = dot(input_vector, self.weights)
        return dot_prod