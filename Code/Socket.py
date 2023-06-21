import socket 
import struct
import Actuator
import time
import json


send_angles=[0,0.0,0.0,0.0]

def open_socket():
    print(" Creating socket....")
    s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('192.168.100.59',8080))
    # s.bind(('169.254.147.120',8080))
    s.listen(3)
    print("socket binded successfully....")
    while True:
        clientsocket,address=s.accept()
        jsonData = json.dumps(send_angles[1:])
        clientsocket.send(jsonData.encode())
        # byte_array = bytearray()
        # print("Actuator deg(socket): ",send_angles[1:])

        # for value in send_angles[1:]:
        #     byte_array.extend(struct.pack('!f', value))
        # print("Socket Transmission....",byte_array)
        # clientsocket.sendall(byte_array)
        time.sleep(0.1)

# def Test_Connection():
#     while True:
#         clientsocket,address=socket.s.accept()
#         print("Connection from:",address,"has been established")
#         clientsocket.send(bytes("Welcome to the socket ","utf-8"))

# def Export_Angles(angles):
#     clientsocket,address=socket.s.accept()
#     angles = [3.14, 2.718, 1.414]
#     byte_array = bytearray()
#     for value in angles:
#         byte_array.extend(struct.pack('!f', value))
#     clientsocket.sendall(byte_array)
    