from numpy import zeros, mean, std, dot, shape, multiply, transpose, add
from feature_extractor.features.neural_networks.NeuralNetwork import NewAssignmentNeuralNetworkBuilder, AssignmentNeuralNetworkWithWeighsBuilder
from numpy.random import randn, standard_normal

class Trainer:
    def __init__(self, layer_input_size, network_layer_depths, fitness_metric, sample_population_size=100, noise_factor=0.05, learning_rate=2):
        self.network_layers_depths = network_layer_depths
        self.layer_input_size = layer_input_size
        self.fitness_metric = fitness_metric
        self.sample_population_size = sample_population_size
        self.noise_factor = noise_factor
        self.learning_rate = learning_rate


    def train(self, fitness_requirement):
        mean_solution = self.get_random_weights_for_network()
        i = 0
        while self.fitness_metric.get_fitness(mean_solution) < fitness_requirement:
            print("Generation", i)
            print("mean solution's accuracy: %s" %
                  (str(self.fitness_metric.get_fitness(mean_solution))))

            sample_candidates = []
            for sample_candidate in range(self.sample_population_size):
                sample_candidates.append(self.get_random_weights_for_network())

            jittered_samples_rewards = zeros(self.sample_population_size)

            for sample_index in range(self.sample_population_size):
                jittered_sample_candidate = add(mean_solution, multiply(self.noise_factor, sample_candidates[sample_index]))
                jittered_samples_rewards[sample_index] = self.fitness_metric.get_fitness(jittered_sample_candidate)

            standardised_rewards = ((jittered_samples_rewards - mean(jittered_samples_rewards))
                                    / std(jittered_samples_rewards))

            mean_solution = (mean_solution
                             + self.learning_rate / (self.sample_population_size * self.noise_factor)
                             * dot(transpose(sample_candidates), standardised_rewards))
            print("mean solution", mean_solution)
            print('\n\n===================================\n')

            i += 1
        print(mean_solution)
        return mean_solution

    def get_random_weights_for_network(self):
        return [standard_normal((layer_depth, layer_input_size)) for layer_input_size, layer_depth in zip(self.layer_input_size, self.network_layers_depths)]


class TrainerFitnessMetric:
    def __init__(self, labeled_samples):
        self.labeled_samples = labeled_samples

    def get_fitness(self, candidate_weights):
        candidate_network = self.get_candidate_network(candidate_weights)
        responses_accuracy = []
        for sample_label, sample_input in self.labeled_samples:
            candidate_response = candidate_network.think(sample_input)
            responses_accuracy.append(candidate_response[sample_label])

        print("resonses accuracy", responses_accuracy)
        return sum(responses_accuracy)

    def get_candidate_network(self, network_weights):
        sample_types = [1, 2, 3, 4, 5, 6, 7, 8, 9, 100, 200, 300]
        hidden_layer_weights = []
        for layer_weights in network_weights[:-1]:
            hidden_layer_weights.append(layer_weights)

        output_layer_data = dict()
        output_layer_weights = network_weights[-1]
        for sample_type, neuron_weights in zip(sample_types, output_layer_weights):
            output_layer_data.update({sample_type: neuron_weights})

        return AssignmentNeuralNetworkWithWeighsBuilder(hidden_layer_weights, output_layer_data).build()