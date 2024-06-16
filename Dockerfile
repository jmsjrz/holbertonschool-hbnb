# This Dockerfile sets up a Python environment and installs the necessary dependencies for running a Flask application.

FROM python:3.10-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file to the working directory
COPY requirements.txt requirements.txt

# Install the Python dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project directory to the working directory
COPY . .

# Set the command to run the Flask application
CMD ["python", "0.0.0.0:5000", "run.py"]
