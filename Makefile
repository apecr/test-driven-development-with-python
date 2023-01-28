.PHONY: test
test: ## Unit tests
	@pytest -vv lists


.PHONY: functional_test
functional_test: ## Start bash session inside container
	@echo "Execute functional tests"
	pytest -vv functional_tests


.PHONY: start
start: # Start the django application
	@echo "Start local app"
	python manage.py runserver
