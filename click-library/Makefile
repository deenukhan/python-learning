install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	black *.py

lint:
	pylint --disable=R,C,E1120 *.py

tests:
	pytest -s -vv test/

all: install format lint tests
	

