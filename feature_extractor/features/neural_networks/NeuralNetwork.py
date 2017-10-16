from feature_extractor.features.neural_networks.Neuron import RectifiedLinearUnit, Neuron, ClassifierRELU

class NeuralNetwork:
    def __init__(self, hidden_layers, output_layer):
        self.hidden_layers = hidden_layers
        self.output_layer = output_layer

    def feed_forward(self, input_vector, layer):
        neuron_outputs = []
        for neuron in layer:
            neuron_outputs.append(neuron.think(input_vector))
        return neuron_outputs

    def think(self, input_vector):
        thinking_vector = input_vector
        for hidden_layer in self.hidden_layers:
            thinking_vector = self.feed_forward(thinking_vector, hidden_layer)
        thinking_vector = self.feed_forward(thinking_vector, self.output_layer)
        return thinking_vector

class DictionaryOutputNeuralNetwork(NeuralNetwork):
    def __init__(self, hidden_layers, output_neurons, output_neuron_keys):
        NeuralNetwork.__init__(self, hidden_layers, output_neurons)
        self.output_neuron_keys = output_neuron_keys

    def think(self, input_vector):
        output_neuron_responses = NeuralNetwork.think(self, input_vector)
        return self.get_output_dictionary(output_neuron_responses)

    def get_output_dictionary(self, output_neuron_responses):
        output_dict = dict()
        for neuron_key, neuron_response in zip(self.output_neuron_keys, output_neuron_responses):
            output_dict.update({neuron_key : neuron_response})
        return output_dict

class LayerBuilder:
    def __init__(self, activation_function):
        self.activation_function = activation_function

    def build(self, neurons_weights):
        return [self.get_new_neuron(neuron_weights) for neuron_weights in neurons_weights]

    def get_new_neuron(self, neuron_weights):
        return Neuron(neuron_weights, self.activation_function)

class SymbolRecognitionNeuralNetworkBuilder:
    def __init__(self, hidden_layers_weights, output_neurons_weights, output_neurons_keys):
        self.hidden_layers_weights = hidden_layers_weights
        self.output_neurons_weights = output_neurons_weights
        self.output_neurons_keys = output_neurons_keys

    def build(self):
        hidden_layers = []
        for hidden_layer_weights in self.hidden_layers_weights:
            hidden_layers.append(LayerBuilder(RectifiedLinearUnit()).build(hidden_layer_weights))
        output_layer = LayerBuilder(RectifiedLinearUnit()).build(self.output_neurons_weights)#[Neuron(neuron_weights, RectifiedLinearUnit()) for neuron_weights in self.output_neurons_weights]#LayerBuilder(RectifiedLinearUnit).build(self.output_neurons_weights)
        network = DictionaryOutputNeuralNetwork(hidden_layers, output_layer, self.output_neurons_keys)
        return network