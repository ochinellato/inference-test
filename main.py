import time
import os
import socket

print("Long running script start")

time.sleep(5)

client_socket = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
client_socket.connect('/tmp/inference-test')
client_socket.send("SENT FROM PYTHON")

time.sleep(5)

print("end long running script")

