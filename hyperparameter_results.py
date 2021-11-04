import rasa
import os
from rasa.nlu.model import Interpreter
import pandas as pd

test_set = pd.DataFrame({'utterance': ['hello', 'hiya', 'hi', 'no'], 'cls': ['greet', 'greet', 'greet', 'deny']})

config = ['config1.yml', 'config2.yml']
training_files = 'data/'
domain = 'domain.yml'
output = 'models/'

for c in config:
    print('-'*5 + f'{c}' + '-'*5)
    model_path = rasa.train(domain, c, training_files, output, force_training=True)
    os.system(f'mkdir models\{model_path.model[7:-7]}_model')  # backslash for windows
    os.system(f'tar -C models/{model_path.model[7:-7]}_model -xvzf {model_path.model}')
    model = Interpreter.load(f'models/{model_path.model[7:-7]}_model/nlu')

    test = test_set.copy()
    test['rasa_intent'] = [model.parse(x)['intent']['name'] for x in test['utterance']]
    test['rasa_confidence'] = [model.parse(x)['intent']['confidence'] for x in test['utterance']]

    test['rasa_accuracy'] = test.apply(lambda x: 1 if x['cls'] == x['rasa_intent'] else 0, axis=1)

    print(f"Accuracy: {sum(test['rasa_accuracy']) / len(test['rasa_accuracy']) * 100:.2f}%")
