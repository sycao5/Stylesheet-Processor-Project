
import yaml


class GraphDataProcessor:
    def __init__(self, filePath):
        self.filePath = filePath

    def readYaml(self):
        with open(self.filePath, 'rt') as f:
            data = f.read()
        return yaml.load(data)



#if __name__ == '__main__':
#    graphDataProcessor = GraphDataProcessor('../../resources/examples/simulate_data_collection/test/combined.yaml')
#    graphDataProcessor.readYaml()

