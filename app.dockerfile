# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Upgrade pip
RUN python -m pip install --upgrade pip

# Set the working directory
WORKDIR /home

# Copy the requirements.txt file into the container
COPY requirements.txt /home

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the application code into the container
COPY src/app /home

# Expose the port the app runs on
EXPOSE 8501

