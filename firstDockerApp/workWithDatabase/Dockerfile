FROM python:3.7.4-slim-buster

# Set the working directory to /app
WORKDIR /app

RUN apt-get update && pip install --upgrade pip
RUN pip install redis

# Copy the current directory contents into the container at /app
COPY . .

CMD ["python3", "app.py"]