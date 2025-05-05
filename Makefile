.PHONY: install test test-coverage lint selfcheck check build

# Installing the package
package-install:
	uv tool install -e .

# Building the package
build:
	uv build

lint:
	uv run ruff check
