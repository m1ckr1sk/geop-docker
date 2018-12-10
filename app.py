from flask import Flask, request, jsonify
from azure.storage.queue import QueueService
import os
import socket
import subprocess

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def hello():
    if request.method == 'GET':
        html = "<h3>OGR says</h3>" \
               "<code>{ogrresult}</code>"
        return html.format(ogrresult=ogrresult())
    if request.method == 'POST':
        data = request.form # a multidict containing POST data
        html = "<p>Received:</p>" \
               "<code>{data}</code>" \
               "<h3>OGR says</h3>" \
               "<code>{ogrresult}</code>"
        return html.format(ogrresult=ogrresult(), data=data)

def pull_from_queue():
  queue_service = QueueService(account_name = 'adockertesting3306', account_key = '/8tgYKwEJO9DqTgvbQ/zI3zsvW3R8+rVwizEx4wi2ZkzuCmDjwMdHUPqHIiduGyGdH+D1ZygYQU4iQdN0TcMwQ==')
  queue_name = 'docker-queue-1'
  messages = queue_service.get_messages(queue_name)
  for message in messages:
    print(message.content)
  

def ogrresult():
    try:	
      os.system("echo hello >> /mydata/file")
      return subprocess.check_output(["ogrinfo", "/mydata/point.geojson"])
    except subprocess.CalledProcessError as e:
      return e.output
      
if __name__ == "__main__":
    pull_from_queue()
    app.run(host='0.0.0.0', port=80)
    
