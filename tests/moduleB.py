class Config:
    def __init__(self):
        self.radius= 4

class Model:
    def __init__(self, conf=Config()):
        self.radius = conf.radius

    def describe(self):
        return("I am a circle r: {}".format(self.radius))

class ProcessorConfig:
    def __init__(self):
        self.nTimes = 5
        
class Processor:
    def __init__(self, config=ProcessorConfig()):
        self.nTimes = config.nTimes

    def process(self, x):
        return (x*self.nTimes)
