install:
	poetry install

build:
	@poetry build

publish: build
	poetry publish -r testpypi
