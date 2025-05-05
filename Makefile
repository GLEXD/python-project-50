# Install dependencies
install:
	uv sync

# Installing the package
package-install:
	uv tool install -e .

# Run tests
test:
	uv run pytest

# Run tests with coverage report
test-coverage:
	uv run pytest --cov=hexlet_python_package --cov-report xml

# Building the package
build:
	uv build

# Run lint
lint:
	uv run ruff check

.PHONY: install test lint selfcheck check build