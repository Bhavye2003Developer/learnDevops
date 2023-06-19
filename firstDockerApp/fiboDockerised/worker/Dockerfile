FROM python:3.7-slim

# Install dependencies
RUN apt-get update && pip install --upgrade pip

# Set working directory
WORKDIR /app

# Copy source code
COPY . /app

CMD ["python", "fiboAlgo.py"]