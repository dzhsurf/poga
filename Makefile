.PHONY:
.DEFAULT_GOAL := help

SRC_DIRS := src tests
define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

.PHONY: help
help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

# .PHONY: lint
# lint: format-check pylint mypy ## Run all lint task

# .PHONY: pylint
# pylint:
# 	poetry run pylint --unsafe-load-any-extension=y -j 0 $(SRC_DIRS) --disable=C0114,C0115,C0116

.PHONY: format-check
format-check: ## Just check format
	poetry run black $(SRC_DIRS) --check

.PHONY: format
format: ## Black & isort the code
	poetry run black $(SRC_DIRS)
	poetry run isort $(SRC_DIRS)

# .PHONY: pydoc
# pydoc:
# 	poetry run pydocstyle renaissance

# .PHONY: mypy
# mypy:
# 	poetry mypy $(SRC_DIRS)

.PHONY: gendocs
gendocs:
	sphinx-apidoc -o docs/source src/poga

.PHONY: docs
docs:
	sphinx-build -b html docs/source docs/build/html

.PHONY: localinstall
localinstall:
	pip install -e .

.PHONY: demo
demo:
	poetry run bash -c 'cd src/example/ && python main.py'

