.PHONY: setup
setup:
	pip install -r requirements.txt

.PHONY: testall
testall: setup
	pip install flake8
	pip install pytest
	pytest .
	@flake8


.PHONY: run
run: testall
	uvicorn main:app --reload
