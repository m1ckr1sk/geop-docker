# Use an official Python runtime as a parent image
FROM gdalalpinepy

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

RUN apk add build-base
RUN pip install --upgrade pip
RUN pip install azure-storage-queue


EXPOSE 80

CMD ["ogrinfo"]

CMD ["python", "app.py"]

