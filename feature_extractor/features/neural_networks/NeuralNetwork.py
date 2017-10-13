from feature_extractor.features.neural_networks.Neuron import RectifiedLinearUnit, Neuron, ClassifierRELU
from numpy.random import randn

class NeuralNetwork:
    def __init__(self, hidden_layers, output_layers):
        self.hidden_layers = hidden_layers
        self.output_layers = output_layers
        #input  layer
        #16 * 16
        #hidden layers
        #output layer
        #output layer contains probablityities for each sample set

    def feed_forward(self, input_vector, layer):
        neuron_outputs = []
        for neuron in layer:
            neuron_outputs.append(neuron.think(input_vector))
        return neuron_outputs

    def get_output_dictionary(self, input_vector, layer):
        output_dict = dict()
        neuron_responses = [neuron.think(input_vector) for neuron in layer]
        for neuron_response in neuron_responses:
            output_dict.update(neuron_response)
        return output_dict

    def think(self, input_vector):
        thinking_vector = input_vector#self.feed_forward(input_vector, self.input_layer)

        for hidden_layer in self.hidden_layers:
            thinking_vector = self.feed_forward(thinking_vector, hidden_layer)

        #for output_layer in self.output_layers:
        thinking_vector = self.get_output_dictionary(thinking_vector, self.output_layers)
       # thought = max(thinking_vector[0], key=thinking_vector[0].get)
        #print("neural network thinks this is the answer", thought)
        #return  dict({thought : thinking_vector[thought]}) #return thinking_vector
        return thinking_vector

class AssignmentNeuralNetwork(NeuralNetwork):
    def __init__(self, hidden_layers, output_layers):
        NeuralNetwork.__init__(self, hidden_layers, output_layers)

class NewAssignmentNeuralNetworkBuilder:
    def __init__(self, sample_types, number_of_hidden_layers):
        self.depth_of_each_layer = number_of_hidden_layers
        self.sample_types = sample_types

 #   def get_new_relu_neuron(self):
  #      return Neuron(randn(16, 1), RectifiedLinearUnit())

   # def get_new_sample_classifier_neuron(self, class_type):
    #    return Neuron(randn(16, 1), ClassifierFunction(class_type))

#TODO get actual number for length of each layer
    def build(self):
        hidden_layers = []
        for depth_of_layer in self.depth_of_each_layer:
            hidden_layers.append(LayerBuilder(RectifiedLinearUnit).build(self.get_new_weights_for_neuron(depth_of_layer)))

        output_layer = LayerBuilder(ClassifierRELU).build(self.get_new_weights_for_neuron(len(self.sample_types)),
                                                          self.sample_types)
        return AssignmentNeuralNetwork(hidden_layers, output_layer)

    def get_new_weights_for_neuron(self, number_of_weights_to_generate):
        return randn(number_of_weights_to_generate)

class LayerBuilder:
    def __init__(self, activation_function):
        self.activation_function = activation_function

    def build(self, neurons_weights, activation_function_args = None):
        return [self.get_new_neuron(neuron_weights, activation_function_args) for neuron_weights in neurons_weights]

    def get_new_neuron(self, neuron_weights, activation_function_args = None):
        if activation_function_args:
            return Neuron(neuron_weights, self.activation_function(activation_function_args))
        else:
            return Neuron(neuron_weights, self.activation_function())

class AssignmentNeuralNetworkWithWeighsBuilder:
    def __init__(self, hidden_layers_weights, output_layers_data):
        self.hidden_layers_weights = hidden_layers_weights
        self.output_layer = output_layers_data

    def build(self):
        hidden_layers = []
        for hidden_layer_weights in self.hidden_layers_weights:
            hidden_layers.append([Neuron(neuron_weights, RectifiedLinearUnit()) for neuron_weights in hidden_layer_weights])
           # hidden_layers.append(LayerBuilder(RectifiedLinearUnit).build(hidden_layer_weights))

       # output_layer = LayerBuilder(ClassifierFunction).build(list(self.output_layer.values()), list(self.output_layer.keys()))
        output_layer = [Neuron(neuron_weights, ClassifierRELU(neuron_class)) for neuron_class, neuron_weights in self.output_layer.items()]

        network = AssignmentNeuralNetwork(hidden_layers, output_layer)
        return network

