# Use the official Python image as a base image
FROM python:3.12-slim

# Set environment variables
ENV FLASK_APP=server.py
ENV FLASK_RUN_HOST=0.0.0.0

# Set the working directory inside the container
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt /app/

RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . /app/

# Expose the port Flask will run on
EXPOSE 5000

# Command to run the Flask app using gunicorn 
# gunicorn --bind 0.0.0.0:5000 wsgi:app
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "wsgi:app"]
