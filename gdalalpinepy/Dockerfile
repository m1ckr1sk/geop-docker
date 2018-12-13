# Use an official Python runtime as a parent image
FROM alpine

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

RUN apk update

RUN apk add --no-cache --virtual .build-deps \
        build-base \
        bzip2-dev \
        expat-dev \
        gcc \
        gdbm-dev \
        libc-dev \
        libffi-dev \
        libressl-dev \
        linux-headers \
        make \
        ncurses-dev \
        pax-utils \
        readline-dev \
        sqlite-dev \
        tar \
        tk \
        tk-dev \
        zlib-dev

RUN apk add python py-pip
RUN apk add python2-dev
RUN pip install --upgrade pip
RUN pip install azure-storage-queue

RUN apk add libcrypto1.1 --update-cache --repository http://dl-3.alpinelinux.org/alpine/edge/main/ --allow-untrusted
RUN apk add gdal --update-cache --repository http://dl-3.alpinelinux.org/alpine/edge/testing/ --allow-untrusted

