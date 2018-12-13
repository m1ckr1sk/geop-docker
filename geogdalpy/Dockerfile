# Use an official Python runtime as a parent image
FROM geodata/gdal

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

RUN pip install --upgrade pip
RUN pip install azure-storage-queue

