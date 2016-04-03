from Classify import Classify

class Main (object):
    def __init__(self, test_file, training_file):
        with open (test_file) as f:
            lines = f.readlines()
            self.test_list = [line.split() for line in lines]
            self.test_list = [x for x in self.test_list if x != []]
        with open (training_file) as f:
            lines = f.readlines()
            self.training_list = [line.split() for line in lines]
            self.training_list = [x for x in self.training_list if x != []]


def print_to_file(results, file):
    total_elements = len(c.results)
    total_correct =0
    file.write('Actual       Predicted\n')
    for row in c.results:
        file.write('{0}, {1} \n'.format(row[0], row[1]))
        if row[0] == row[1]:
            total_correct += 1
    file.write('total_correct: {0}\n'.format(total_correct))
    file.write('total_elements: {0}\n'.format(total_elements))
    percentage_right = (total_correct/total_elements)*100
    file.write('percentage_right: {0}\n'.format(percentage_right))


if __name__=="__main__":
    data = Main('data/iris-test.txt', 'data/iris-training.txt')
    k = 1
    c = Classify(data, k)
    k1_file = open('../K1_classification.txt', 'w')
    print_to_file(c.results, k1_file)
    k = 3
    c = Classify(data, k)
    k3_file = open('../K3_classification.txt', 'w')
    print_to_file(c.results, k3_file)
