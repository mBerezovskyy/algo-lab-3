import csv


class Solution:
    def __init__(self):
        self.number_of_layers = 0
        self.layers_of_graph = []

    def read_file(self, filename):
        with open(filename) as data:
            csv_reader = csv.reader(data, delimiter=" ")
            next(csv_reader)
            for row in csv_reader:
                self.layers_of_graph.append(list(map(lambda x: int(x), row)))
            self.number_of_layers = len(self.layers_of_graph)

    def find_the_longest_career_path(self, layer, element):
        current_left = self.layers_of_graph[layer + 1][element]
        curent_right = self.layers_of_graph[layer + 1][element + 1]
        if current_left > curent_right:
            self.layers_of_graph[layer][element] += current_left
        else:
            self.layers_of_graph[layer][element] += curent_right

    def find_maximum_experience(self):
        for layer in range(self.number_of_layers - 2, -1, -1):
            for element in range(layer + 1):
                self.find_the_longest_career_path(layer, element)
        return self.layers_of_graph[0][0]
