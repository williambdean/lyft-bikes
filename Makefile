format: 
	python -m black divvy tests setup.py

clean: 
	find divvy tests | grep -E "(/__pycache__$\|\.pyc$\|\.pyo$\)" | xargs rm -rf

test: 
	python -m pytest tests

coverage: 
	python -m pytest --cov-report html --cov=divvy tests/ && open htmlcov/index.html

export: 
	conda env export > environment.yaml
