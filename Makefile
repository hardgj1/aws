install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	pylint --disable=R,C,E1120 telco.py telco2.py
	

format:
	black hellodetect.py