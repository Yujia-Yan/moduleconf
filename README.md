# ModuleConf

A minimal module-specific configuration tool for fast experimenting.



## Installation

> pip3 install moduleconf
> 
> 

## Module and Module specific configuration

For each module, we may have some configuration classes that only apply to that module. 
However, we often need to experiment with a variety of alternate modules that may contain serveral different module configurations.
This simple library helps with automatically load modules based on the configuration file and also automatically generate templates for creating a new configuration file.

## Basic Usage

In moduleA.py, we defined a Model and its Configuration class/prototype

```python
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

```

In moduleB.py. Similarly:

```python
class Config:
    def __init__(self):
        self.radius= 4

class Model:
    def __init__(self, conf=Config()):
        self.radius = conf.radius

    def describe(self):
        return("I am a circle r: {}".format(self.radius))

```

We then generate the config template for use:

> python3 -m moduleconf.generate model:moduleA:Config >> confA.json
> 
> python3 -m moduleconf.generate model:moduleB:Config >> confB.json



It will generate confA.json and confB.json, each containing specific options according to the config prototy defined in the module:

In confA.json:

```json
{
	"model": {
		"module": "moduleA",
		"configClassName": "Config",
		"config": {
			"height": 5,
			"width": 3
		}
	}
}
```

In confB.json:

```json
{
	"model": {
		"module": "moduleB",
		"configClassName": "Config",
		"config": {
			"radius": 4
		}
	}
}
```

Then the conf file can be parsed into a ModuleConf object. For the ModuleConf object, we can use conf.module to refer to the module the configuration where has been defined, and we can access the configuration object by conf.config:

```python
import moduleconf
import json
import sys
import os


# add path to import the module from
sys.path.append(os.path.join(os.path.dirname(__file__), '.'))

confPath = "./confA.json"
# or
confPath = "./confB.json"

with open(confPath, 'r') as f:
    conf = moduleconf.parse(json.load(f))

    # load the model
    model = conf["model"].module.Model(conf["model"].config)
    print(model.describe())
```

Make sure the module defined should be importable in the current search path. Here it adds the module path to the import path:

> sys.path.append(os.path.join(os.path.dirname(**file**), '.'))



### Support for configuration class containing complex type

STUB

### Support for nested configuration file

STUB
