# parent image
# updated
FROM python:3.7-slim



RUN pip install --trusted-host pypi.python.org pymssql

RUN pip install flask

RUN pip install flask-restful

RUN pip install flask-cors

COPY requirements.txt requirements.txt

COPY app.py app.py

RUN set FLASK_APP=app.py

CMD ["flask", "run", "--host", "0.0.0.0"]

