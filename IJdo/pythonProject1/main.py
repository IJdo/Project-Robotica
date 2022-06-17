import socket
import sys
from struct import unpack
import numpy as np
from PIL import Image

class UDP_receiver:
    def __init__(self, host, port): #make sure host and port are the same as the sender
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.host = host
        self.port = port
        self.server_address = (host, port)
        print(f'Starting UDP server on {host} port {port}')
        self.sock.bind(self.server_address)

    def unpack(self):
        message, address = UDP_receiver.sock.recvfrom(4096)
        print(f'Received {len(message)} bytes:')
        return unpack('2f', message)


class data_point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


if __name__ == '__main__':
    y = 0
    UDP_receiver = UDP_receiver('192.168.178.178', 65000) # pc ijdo, 192.168.55.128 mobiele hotspot ijdo
    map = np.zeros((300,300))
    huidige_richting = 0
    robotLocatie = data_point(0,0)
    muurLocatie = data_point(0,0)

    #afstand in 1 sec is 70 cm.
    #elke lezing = y + 10.
    reading = UDP_receiver.unpack()
    robotLocatie.x = robotLocatie.x + reading[0]
    print(f'Distance: {reading[0]}', f'Odometry: {reading[1]}')
    for i in range(10):

        reading = UDP_receiver.unpack()
        print(f'Distance: {reading[0]}', f'Odometry: {reading[1]}')
        huidige_richting += reading[1]
        print(f"richting: {huidige_richting}")

        if huidige_richting == 0:
            robotLocatie.y = robotLocatie.y + 10
            muurLocatie.y = robotLocatie.y
            muurLocatie.x = robotLocatie.x - reading[0] #fix issue with varying sensor data (40-41 = -1)
            if muurLocatie.x < 0:
                muurLocatie.x = 0
            print(f"robot x: {robotLocatie.x}", f"robot y: {robotLocatie.y}", f"muurlocatie x = {muurLocatie.x}", f"muurlocatie y: {muurLocatie.y}")

            map[int(robotLocatie.y)][int(robotLocatie.x)] = 255
            map[int(muurLocatie.y)][int(muurLocatie.x)] = 155 #naar voren rijden
        elif huidige_richting == 270:
            robotLocatie.x = robotLocatie.x + 10
            muurLocatie.x = muurLocatie.x +10
            muurLocatie.y = robotLocatie.y + reading[0]
            map[int(robotLocatie.y)][int(robotLocatie.x)] = 255
            map[int(muurLocatie.y)][int(muurLocatie.x)] = 155 #naar rechts rijden


    img = Image.fromarray(map)
    img.show()


    # while True:
    #     x = UDP_receiver.unpack()
    #     print(f'Distance: {x}')
