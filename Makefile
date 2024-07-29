clean:
	find lyft_bikes tests | grep -E "(/__pycache__$\|\.pyc$\|\.pyo$\)" | xargs rm -rf

test:
	poetry run python -m pytest tests

html:
	poetry run mkdocs serve
