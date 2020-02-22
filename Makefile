publish:
	 poetry publish -r pypi-test

install:
	poetry install

test:
	poetry run pytest gendiff tests

lint:
	poetry run flake8 gendiff

selfcheck:
	poetry check

check: selfcheck test lint

build:
	poetry build

.PHONY: install lint selfcheck check build