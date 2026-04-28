.PHONY: help install test lint format build clean publish

help:
	@echo "fogsift-icarus dev commands:"
	@echo "  install   Install package + dev deps via uv"
	@echo "  test      Run pytest with coverage"
	@echo "  lint      Run ruff check"
	@echo "  format    Run ruff format"
	@echo "  build     Build sdist + wheel"
	@echo "  clean     Remove build artifacts"
	@echo "  publish   Publish to PyPI (needs UV_PUBLISH_TOKEN)"

install:
	uv pip install -e ".[dev]"

test:
	uv run pytest tests/ -v --cov=fogsift_icarus --cov-report=term-missing

lint:
	uv run ruff check .
	uv run ruff format --check .

format:
	uv run ruff format .
	uv run ruff check --fix .

build: clean
	uv build

clean:
	rm -rf dist/ build/ *.egg-info src/*.egg-info .pytest_cache .coverage htmlcov

publish: build
	uv publish
