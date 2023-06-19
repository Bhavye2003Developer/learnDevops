FROM python:3.7-slim

# Install dependencies
RUN apt-get update && pip install --upgrade pip
RUN pip install Django

# Set working directory
WORKDIR /app

# Copy source code
COPY . /app
EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]