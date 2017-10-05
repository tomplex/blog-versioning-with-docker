FROM python:3.6

copy . /flask

RUN pip install -r /flask/requirements.txt

ENTRYPOINT  ["python", "/flask/basic_flask_app.py"]

