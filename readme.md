# Alpine
sudo docker build -t gdalalpinepyapp .
sudo docker build -t gdalalpinepyapp .

sudo docker run -v /home/pi/gdal/mydata:/mydata gdalalpinepyapp

# Geodata/gdal
sudo docker build -t geogdalpy .
sudo docker build -t geogdalpyapp .

sudo docker run -ti -v /home/docker/Documents/geop-docker/data:/mydata geogdalpyapp

