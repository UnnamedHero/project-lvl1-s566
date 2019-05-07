install:
	poetry install

build:
	@poetry build

publish: build
	poetry publish -r testpypi

lint:
	poetry run flake8 brain_games
