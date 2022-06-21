import socket
import sys
from struct import unpack
from PIL import Image
import numpy as np


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

class _mapMuren:
    def __init__(self, map):
        for i in range((map.width - 1)):
            map.map[0][i] = 255 # muurAchter
        for i in range((map.height - 1)):
            map.map[i][0] = 255 # muurLinks
        for i in range((map.width - 1)):
            map.map[map.height - 1][i] = 255 #muurVoor
        for i in range((map.height - 1)):
            map.map[i][map.width - 1] = 255 #muurRechts
class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.map = np.zeros((self.height, self.width), dtype=np.uint8) #numpy array goes [height][width]

class _mapRobot:
    def __init__(self, map, dist_frnt, dist_lft, dist_rght):
        self.initial_dist_frnt = dist_frnt
        self.initial_dist_lft = dist_lft
        self.initial_dist_rght = dist_rght
        x = ((0 + dist_lft)+(map.width - dist_rght))/2 # bepaal midden van robot op locatie (x,0). Werkt alleen als er geen objecten naast de robot zijn.
        y = ((map.height - dist_frnt)) #bepaal y van de robot (werkt alleen als er initieel geen objecten voor de robot zijn
        self.location = data_point(x,y) #robot start altijd in de hoek
        map.map[self.location.y][self.location.x] = 200 #plaats de robot op de kaart
        self.orientatie = 0 #zet de orientatie van de robot op 0
        self.obstacle = data_point(0,0) #maak een object aan voor het tekeken van de data punten waar de robot niet kan rijden.

    def update_robot(self, distance_front, distance_left, distance_right, distance_traveld):# rechtdoor rijden, depth first algoritme.
        if self.orientatie == 0:
            if ((distance_right + distance_left)*1.1) < map.width: #check for objects
                if (distance_right * 1.1) < self.initial_dist_rght: #obstakel rechts van de robot. als gemeten afstand +10% < initiale afstand
                    self.location.x = self.location.x
                    self.location.y = self.location.y + distance_traveld
                    self.obstacle.x = self.location.x + distance_right
                    self.obstacle.y = self.location.y
                    map.map[self.location.y][self.location.x] = 200
                    map.map[self.obstacle.y][self.obstacle.x] = 255
                elif (distance_left * 1.1) < self.initial_dist_lft: #obstakel links van de robot.
                    self.location.x = self.location.x
                    self.location.y = self.location.y + distance_traveld
                    self.obstacle.x = self.location.x - distance_left
                    self.obstacle.y = self.location.y
                    map.map[self.location.y][self.location.x] = 200
                    map.map[self.obstacle.y][self.obstacle.x] = 255
                else:
                    self.location.x = self.location.x
                    self.location.y = self.location.y + distance_traveld
            else:
                self.location.x = self.location.x
                self.location.y = self.location.y + distance_traveld



            # x_offset_right = 300 - distance_right # bereken locatie rechter sensor
            # x_offset_left = 0 + distance_left # bereken locatie linker sensor
            # x_offset_true = (x_offset_right + x_offset_left)/2 # pak het midden van de twee locaties.
            # self.location.y = 300 - distance_front #elke keer dat de robot naar voren rijdt moet de update functie uitgevoerd worden.
            # self.location.x = MuurLinks
        if self.orientatie == 90:
            pass
            #doe iets.
        if self.orientatie == 180:
            pass
        if self.orientatie == 270:
            pass


        # self.location.x = 0 + x_offset_true


        print(self.location.x)
        print(self.location.y)
        map.map[int(self.location.y)][int(self.location.x)] = 100
        map.map[int(self.location.y + (distance_front - 1))][int(self.location.x)] = 255
        map.map[int(self.location.y)][int(self.location.x + distance_right)] = 255
        map.map[int(self.location.y)][int(self.location.x - distance_left)] = 255

    # def update_obstacles(self, distance_front, distance_left, distance_right, distance_traveld, odometry):
    #     if odometry is 0:
    #
    #
    #     self.map[int(self.obstacle.y)][int(self.obstacle.y)] = 255

    def open_map(self):
        img = Image.fromarray(map.map)
        img.show()


if __name__ == '__main__':
    map = Map(300, 300)
    UDP_receiver = UDP_receiver('192.168.178.178', 65000)  # pc ijdo, 192.168.55.128 mobiele hotspot ijdo
    maprobot = _mapRobot(map)
    # for x in range(200):
    #     maprobot.update_robot((280 - x), 265, 25, 0, 0)
    #
    # maprobot.open_map()
    mapmuren = _mapMuren(map)
    maprobot.open_map()


