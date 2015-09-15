
import yaml


class StylesheetYamlProcessor:
    def __init__(self, filePath):
        self.filePath = filePath

    def readYaml(self):
        with open(self.filePath, 'rt') as f:
            data = f.read()
        return yaml.load(data)





