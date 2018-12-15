.PHONY: clean train-nlu train-core cmdline server

TEST_PATH=./

train-nlu:
	python -m rasa_nlu.train -c nlu_config.yml --data data/nlu_data.md -o models --fixed_model_name nlu --project current --verbose

train-core:
	python -m rasa_core.train -d domain.yml -s data/stories.md -o models/current/dialogue -c policies.yml

run-core:
	python -m rasa_core.run -d models/current/dialogue -u models/current/nlu

run-nlu:
	python -m rasa_nlu.run -m models/current/nlu

interactive:
	python -m rasa_core.train interactive -o models/current/dialogue -d domain.yml -s data/stories.md --nlu models/current/nlu --endpoints endpoints.yml

action-server:
	python -m rasa_core_sdk.endpoint --actions actions
