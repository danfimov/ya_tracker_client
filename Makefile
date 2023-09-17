args := $(wordlist 2, 100, $(MAKECMDGOALS))

APPLICATION_NAME = ya_tracker_client

HELP_FUN = \
	%help; while(<>){push@{$$help{$$2//'options'}},[$$1,$$3] \
	if/^([\w-_]+)\s*:.*\#\#(?:@(\w+))?\s(.*)$$/}; \
    print"$$_:\n", map"  $$_->[0]".(" "x(20-length($$_->[0])))."$$_->[1]\n",\
    @{$$help{$$_}},"\n" for keys %help; \

CODE = ya_tracker_client
TEST = poetry run python3 -m pytest --verbosity=2 --showlocals --log-level=DEBUG

ifndef args
MESSAGE = "No such command (or you pass two or many targets to ). List of possible commands: make help"
else
MESSAGE = "Done"
endif


help: ##@Help Show this help
	@echo -e "Usage: make [target] ...\n"
	@perl -e '$(HELP_FUN)' $(MAKEFILE_LIST)

install:  ##@Setup Install project requirements
	python3 -m pip install poetry
	poetry install

test:  ##@Testing Test application with pytest
	$(TEST)

test-cov:  ##@Testing Test application with pytest and create coverage report
	$(TEST) --cov=$(APPLICATION_NAME) --cov-report html --cov-fail-under=85

lint:  ##@Code Check code with pylint
	poetry run python3 -m ruff $(CODE) tests

format:  ##@Code Reformat code with ruff and black
	poetry run python3 -m ruff $(CODE) tests --fix

clean:  ##@Code Clean directory from garbage files
	rm -fr *.egg-info dist
