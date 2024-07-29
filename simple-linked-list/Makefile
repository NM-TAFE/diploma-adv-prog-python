# Define paths and settings
SRC := src
TESTS := tests

# Targets
.PHONY: all install_requirements mypy test lint clean

# Default target
all: install_requirements mypy test flake8

# Install Python dependencies from requirements.txt
install_requirements:
	pip install mypy flake8

# Run mypy static type check
mypy: export MYPYPATH=$(SRC)/
mypy:
	mypy src/ --enable-incomplete-feature=NewGenericSyntax --explicit-package-bases

# Run unittests with discovery
test: export PYTHONPATH=$(SRC)
test:
	python -m unittest discover -s $(TESTS)

# Run flake8 linting
lint:
	flake8 $(SRC)

# Clean generated files
clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -exec rm -rf {} +
