format: 
	python -m black divvy tests setup.py

test: 
	python -m pytest tests

export: 
	conda env export > environment.yaml
