'''
Source: https://rasa.com/docs/nlu/quickstart/#
GUI: https://github.com/RasaHQ/rasa-nlu-trainer
Starter-pack: https://github.com/RasaHQ/starter-pack-rasa-nlu
Training: python -m rasa_nlu.train -c nlu_config.yml --data nlu.md -o models --fixed_model_name nlu --project current --verbose
'''

from rasa_nlu.model import Interpreter
import json

def main():
    interpreter = Interpreter.load("./models/current/nlu")
    message = "let's see some italian restaurants"

    result = interpreter.parse(message)

    print(json.dumps(result, indent=2))

if __name__ == '__main__':
    main()

'''
JSON produced from running python main.py:

{
  "entities": [
    {
      "extractor": "ner_crf",
      "confidence": 0.5706574828706044,
      "end": 22,
      "value": "italian",
      "entity": "cuisine",
      "start": 15
    }
  ],
  "intent": {
    "confidence": 0.914196252822876,
    "name": "restaurant_search"
  },
  "text": "let's see some italian restaurants",
  "intent_ranking": [
    {
      "confidence": 0.914196252822876,
      "name": "restaurant_search"
    },
    {
      "confidence": 0.06565813720226288,
      "name": "greet"
    },
    {
      "confidence": 0.04689149558544159,
      "name": "goodbye"
    },
    {
      "confidence": 0.0,
      "name": "affirm"
    }
  ]
}
'''
