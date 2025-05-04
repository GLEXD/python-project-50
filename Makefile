.PHONY: install test test-coverage lint selfcheck check build

# Installing the package
package-install:
	uv tool install -e .

# Building the package
build:
	uv build

#Installing the assembled package
as.-package-install:
	uv tool install dist/*.whl