FROM python:3.7.4-slim-buster

RUN apt-get update -y && apt-get install -y
RUN python -m pip install --upgrade pip
RUN python -m pip install Django
RUN pip install redis

WORKDIR /app
COPY . /app

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]