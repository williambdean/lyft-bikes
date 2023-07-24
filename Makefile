format: 
	poetry run python -m black lyft_bikes tests

clean: 
	find lyft_bikes tests | grep -E "(/__pycache__$\|\.pyc$\|\.pyo$\)" | xargs rm -rf

test: 
	poetry run python -m pytest tests

cov: 
	poetry run python -m pytest --cov-report html --cov=lyft_bikes tests/ && open htmlcov/index.html

html: 
	poetry run mkdocs serve
