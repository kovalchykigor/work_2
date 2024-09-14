# Use an official Python runtime as a parent image
FROM python:3.10.12

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install psycopg2
RUN pip install -r requirements.txt

# Run the app when the container launches
CMD ["pytest", "test_app.py"]
