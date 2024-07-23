# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Upgrade pip
RUN python -m pip install --upgrade pip

# Copy the project file into the container
COPY . /app

# Set the working directory
WORKDIR /app

# Set the PYTHONPATH
ENV PYTHONPATH=/app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Expose the port the app runs on
EXPOSE 8000

# Command to run the app
CMD ["python", "src/api/get_number_visitors_api.py"]


