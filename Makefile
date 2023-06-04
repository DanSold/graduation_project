.PHONY: setup
setup:
	@echo 'start installing'
	pip install pytest flake8
	pip install -r requirements.txt

.PHONY: testall
testall: setup
	pytest .
	@flake8 --extend-ignore E203 \
         --exclude .git,__pycache__,docs/source/conf.py,old,build,dist,venv,trash.py \
         --max-complexity 10 \
         --ignore=E501

.PHONY: test.app
test.app:
	pytest .\\tests\\$(app)

.PHONY: run
run:
	uvicorn main:app --reload
