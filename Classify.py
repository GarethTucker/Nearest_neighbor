import math

class Classify (object):
    def __init__(self, data, k):
        self.feature_range= [0] * (len(data.test_list[0])-1)

        for index, value in enumerate(self.feature_range):

            max_test_value = max(element[index] for element in data.test_list )
            max_training_value = max(element[index] for element in data.training_list)
            max_value = max(max_test_value, max_training_value)

            min_test_value = min(element[index] for element in data.test_list)
            min_training_value = min(element[index] for element in data.training_list)
            min_value = min(min_test_value, min_training_value)

            self.feature_range[index] = float(max_value) - float(min_value)

        self.results = [(element[len(element)-1], self.get_nearest_neighbor(data, element, k)) for element in data.test_list]

    def get_nearest_neighbor(self, data, test_element, k):
        neighbors = []

        for training_element in data.training_list:
            total_weight = 0

            for index, value in enumerate(self.feature_range):
                unweighted_value = (float(test_element[index]) - (float(training_element[index])))**2
                weighted_value = unweighted_value/(self.feature_range[index]**2)
                total_weight += weighted_value
            total_weight = math.sqrt(total_weight)
            neighbors += [[total_weight, training_element[len(training_element)-1]]]
            neighbors.sort(key=lambda x: x[0])

        common_classes = [row[1] for row in neighbors[:k]]
        return max(common_classes, key=common_classes.count)