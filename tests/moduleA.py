class Config:
    def __init__(self):
        self.height = 5
        self.width = 3
        
class Model:
    def __init__(self, conf = Config()):
        self.height = conf.height
        self.width = conf.width
    
    def describe(self):
        return ("I am a rectangle h: {} w: {}".format(self.height, self.width))

class ProcessorConfig:
    def __init__(self):
        pass

class Processor:
    def __init__(self, config = ProcessorConfig()):
        pass
    def process(self, x):
        return (x[::-1])
