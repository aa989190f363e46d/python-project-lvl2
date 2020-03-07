publish:
	 poetry publish -r pypi-test

install:
	poetry install

test:
	poetry run pytest

lint:
	poetry run flake8 gendiff

selfcheck:
	poetry check

check: selfcheck lint test

build:
	poetry build

.PHONY: publish install test lint selfcheck check build