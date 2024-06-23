# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /ideahub

# Copy the requirements file into the container
COPY requirements.txt /ideahub/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . /ideahub/

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run the Django server with the specific settings
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000", "--settings=settings.local"]
