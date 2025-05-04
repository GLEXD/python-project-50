.PHONY: install test test-coverage lint selfcheck check build

# Install packages
packages-install:
	uv tool install -e .
