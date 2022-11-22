import moduleconf
import json
import sys
import os


# add path to import the module from
sys.path.append(os.path.join(os.path.dirname(__file__), '.'))


with open("tests/confA.json", 'r') as f:
    conf = moduleconf.parse(json.load(f))

    # load the model
    model = conf["model"].module.Model(conf["model"].config)
    print(model.describe())
    processor = conf["processor"].module.Processor(
        conf["processor"].config
    )
    print(processor.process(model.describe()))

with open("tests/confA_fields_missing.conf", 'r') as f:
    conf = moduleconf.parse(json.load(f), allowMissing = True)

    # load the model
    model = conf["model"].module.Model(conf["model"].config)
    print(model.describe())
    processor = conf["processor"].module.Processor(
        conf["processor"].config
    )
    print(processor.process(model.describe()))

