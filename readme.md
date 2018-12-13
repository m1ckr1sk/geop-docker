sudo docker build -t gdalalpinepyapp .

sudo docker run -v /home/pi/gdal/mydata:/mydata gdalalpinepyapp
