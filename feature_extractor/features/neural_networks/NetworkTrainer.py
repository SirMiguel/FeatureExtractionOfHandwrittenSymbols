from numpy import zeros, mean, std, dot, multiply, transpose, add
from numpy.random import standard_normal

from feature_extractor.features.neural_networks.NeuralNetwork import SymbolRecognitionNeuralNetworkBuilder


class Trainer:
    def __init__(self, layer_neuron_input_size, layer_depths):
        self.layer_neuron_input_size = layer_neuron_input_size
        self.network_layers_depths = layer_depths

    def train(self, stop_condition):
        raise NotImplementedError("Trainer has no default implementation to train a neural network")


class EvolutionaryTrainer(Trainer):
    def __init__(self, layer_neuron_input_size, layer_depths, fitness_metric):
        Trainer.__init__(self, layer_neuron_input_size, layer_depths)
        self.fitness_metric = fitness_metric

    def train(self, fitness_requirement):
        raise NotImplementedError("Evolutionary Trainer has no default implementation to train a neural network")

    def get_fitness(self, weights):
        return self.fitness_metric.get_fitness(weights)

class NESTrainer(EvolutionaryTrainer):
    def __init__(self, layer_input_size, layer_depths, fitness_metric, sample_population_size=500, noise_factor=0.1, learning_rate=1):
        EvolutionaryTrainer.__init__(self, layer_input_size, layer_depths, fitness_metric)
        self.sample_population_size = sample_population_size
        self.noise_factor = noise_factor
        self.learning_rate = learning_rate

    def train(self, fitness_requirement):
        mean_solution = self.get_random_weights_for_network()
        number_of_generations = 0
        mean_solution_fitness = self.get_fitness(mean_solution)
        while mean_solution_fitness < fitness_requirement:
            self.learning_rate /= 2
            print("Generation", number_of_generations)
            print("mean solution's accuracy:", mean_solution_fitness)

            directions_from_mean = self.get_random_directions()
            direction_rewards = self.get_direction_rewards(directions_from_mean, mean_solution)
            standardised_rewards_of_directions = self.get_standardised_rewards(direction_rewards)
            mean_solution = self.update_mean_solution(directions_from_mean, mean_solution,
                                                      standardised_rewards_of_directions)
            mean_solution_fitness = self.get_fitness(mean_solution)

            print("mean solution", mean_solution)
            print('\n\n===================================\n')

            number_of_generations += 1
        return mean_solution

    def get_direction_rewards(self, directions_from_mean, mean_solution):
        direction_rewards = zeros(self.sample_population_size)
        for sample_index in range(self.sample_population_size):
            direction_headed_from_mean = add(mean_solution,
                                             multiply(self.noise_factor, directions_from_mean[sample_index]))
            direction_rewards[sample_index] = self.get_fitness(direction_headed_from_mean)
            #print("sample", sample_index, "rewards", direction_rewards[sample_index])
        return direction_rewards

    def get_standardised_rewards(self, direction_rewards):
        standardised_rewards_of_directions = (direction_rewards - mean(direction_rewards)) / (std(direction_rewards))#(self.sample_population_size / self.noise_factor )
           # direction_rewards)  # TODO look into noise factor instead of std
        return standardised_rewards_of_directions

    def update_mean_solution(self, directions_from_mean, mean_solution, standardised_rewards_of_directions):
        mean_solution = (mean_solution
                         + self.learning_rate / (self.sample_population_size * self.noise_factor)
                         * dot(transpose(directions_from_mean), standardised_rewards_of_directions))
        return mean_solution

    def get_random_directions(self):
        directions_from_mean = []
        for sample_candidate in range(self.sample_population_size):
            directions_from_mean.append(self.get_random_weights_for_network())
        return directions_from_mean

    def get_random_weights_for_network(self):
        return [standard_normal((layer_depth, layer_input_size)) for layer_input_size, layer_depth in zip(self.layer_neuron_input_size, self.network_layers_depths)]


class FitnessMetric:
    def __init__(self):
        pass

    def get_fitness(self, candidate_weights):
        raise NotImplementedError("There is no default implementation of Fitness Metric")


class AssignmentNeuralNetworkFitnessMetric(FitnessMetric):
    def __init__(self, labeled_samples, sample_types):
        FitnessMetric.__init__(self)
        self.labeled_samples = labeled_samples
        self.sample_types = sample_types

    def get_fitness(self, candidate_weights):
        candidate_network = self.get_candidate_network(candidate_weights)
        responses_accuracy = []
        for sample_label, sample_input in self.labeled_samples:
            candidate_response = candidate_network.think(sample_input)
            candidate_response = max(candidate_response, key=candidate_response.get)
            responses_accuracy.append((1 if candidate_response == sample_label else -1))
        return sum(responses_accuracy)

    def get_candidate_network(self, network_weights):
        hidden_layer_weights = network_weights[:-1]
        output_layer_weights = network_weights[-1]
        return SymbolRecognitionNeuralNetworkBuilder(hidden_layer_weights, output_layer_weights, self.sample_types).build()