from azure.storage.queue import QueueService
import os
import socket
import subprocess

def pull_from_queue():
  queue_service = QueueService(account_name = 'adockertesting3306', account_key = '/8tgYKwEJO9DqTgvbQ/zI3zsvW3R8+rVwizEx4wi2ZkzuCmDjwMdHUPqHIiduGyGdH+D1ZygYQU4iQdN0TcMwQ==')
  queue_name = 'docker-queue-1'
  messages = queue_service.get_messages(queue_name)
  for message in messages:
    result = ogrresult()
    print(result + " " + message.content)
  

def ogrresult():
    try:	
      os.system("echo hello >> /mydata/file")
      return subprocess.check_output(["ogr2ogr", "-f", "GPKG", "/mydata/output.gpkg", "/mydata/OSOpenGreenspace_SU.gml"])
    except subprocess.CalledProcessError as e:
      return e.output
      
if __name__ == "__main__":
    pull_from_queue()
    
