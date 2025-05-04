args := $(wordlist 2, 100, $(MAKECMDGOALS))

.DEFAULT:
	@echo "No such command (or you pass two or many targets to ). List of possible commands: make help"

.DEFAULT_GOAL := help

##@ Local development

.PHONY: help
help: ## Show this help
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target> <arg=value>\033[0m\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m  %s\033[0m\n\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

.PHONY: install
install: ## Install project requirements
	@uv sync --all-extras

##@ Testing and formatting

.PHONY: test
test: ## Test application with pytest
	@pytest --verbosity=2 --showlocals --log-level=DEBUG

.PHONY: test-cov
test-cov: ## Test application with pytest and create coverage report
	@pytest --verbosity=2 --showlocals --log-level=DEBUG --cov=ya_tracker_client --cov-report html --cov-fail-under=85 --cov-config pyproject.toml

.PHONY: lint
lint: ## Check code with ruff
	@ruff check ya_tracker_client examples tests

.PHONY: format
format: ## Reformat code with ruff
	@ruff format ya_tracker_client examples tests

.PHONY: precommit
precommit: ## Check code with pre-commit hooks
	@pre-commit run --all-files

.PHONY: clean
clean: ## Clean directory from garbage files
	@rm -fr *.egg-info dist
