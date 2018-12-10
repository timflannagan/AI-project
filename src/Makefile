train-nlu:
	python -m rasa_nlu.train -c ../rasa/nlu_config.yml --data ../rasa/nlu.md -o models --fixed_model_name nlu --project current --verbose

train-core:
	python -m rasa_core.train -d ../rasa/domains.yml -s ../rasa/data/stories.md -o ../models/current/dialogue

core-learn:
	python -m rasa_core.train interactive -o ../models/current/dialogue -d ../rasa/domains.yml -s ../rasa/data/stories.md -u ../models/current/nlu --endpoints ../rasa/data/endpoints.yml
