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
        return unpack('5f', message)

    def end(self):
        message, address = UDP_receiver.sock.recvfrom(4096)
        print(f'Received {len(message)} bytes:')
        return unpack('1i', message)

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
        self.distance_till_end = dist_frnt
        self.distance_left_vorige = dist_left
        self.distance_right_vorige = dist_right
        self.total_distance_travelled_0 = 0
        self.total_distance_travelled_90 = 0
        self.total_distance_travelled_180 = 0
        self.total_distance_travelled_270 = 0
        #self.initial_dist_lft = dist_lft
        #self.initial_dist_rght = dist_rght
        #x = 30 # bepaal midden van robot op locatie (x,0). Werkt alleen als er geen objecten naast de robot zijn.
        #y = 40 #((map.height - dist_frnt)) #bepaal y van de robot (werkt alleen als er initieel geen objecten voor de robot zijn.. is 12 omdat robot 25cm is /2  = 12,5
        x = 0 + dist_rght
        y = (map.height - dist_front)
        self.location = data_point(x,y) #robot start altijd in de hoek
        map.map[int(self.location.y)][int(self.location.x)] = 100 #plaats de robot op de kaart
        self.orientatie = 0 #zet de orientatie van de robot op 0
        self.obstacle = data_point(0,0) #maak een object aan voor het tekeken van de data punten waar de robot niet kan rijden.
        self.orientatie_last = 0

    def update_robot(self, distance_front, distance_left, distance_right, odometry, reciever):# rechtdoor rijden, depth first algoritme.
        self.orientatie = odometry
        if self.orientatie == 0:
            afgelegde_afstand = self.initial_dist_frnt - distance_front
            self.location.y = self.location.y + afgelegde_afstand
            #self.location.x = ((map.width - distance_right)+(0 + distance_left))/2
            #distance_left + distance_right = 300
            if (distance_left*1.15) < self.distance_left_vorige:
                self.location.x = (map.width - dist_right)
                self.obstacle.x = self.location.x + distance_left
                self.obstacle.y = self.location.y
                map.map[int(self.obstacle.y)][int(self.obstacle.x)] = 255
                #er zit een object aan de linker kant
            elif (distance_right*1.15) < self.distance_right_vorige:
                print(distance_right)
                print(self.distance_right_vorige)
                self.location.x = (0 + distance_left)
                self.obstacle.x = self.location.x - distance_right
                self.obstacle.y = self.location.y
                print(self.obstacle.x)
                print(self.obstacle.y)
                map.map[int(self.obstacle.y)][int(self.obstacle.x)] = 255
            else:
                # er zit geen object
                self.location.x = (0 + distance_right)
                pass

            map.map[int(self.location.y)][int(self.location.x)] = 100
            self.distance_left_vorige = distance_left
            self.distance_right_vorige = distance_right

            # if self.orientatie_last != 0: #check of laatste orientatie richting anders was.
            #     x = reciever.unpack()
            #     self.distance_till_end = x[0]
            #     self.total_distance_travelled_0 = 0
            #
            # distance_travelled = self.distance_till_end - distance_front        # bereken afgelegde afstand aan de hand van de voor sensor.
            # self.total_distance_travelled_0 = self.total_distance_travelled_0 + distance_travelled
            # self.distance_till_end = distance_front
            # self.location.y = self.location.y + distance_travelled  # bereken nieuwe y locatie in de map
            # self.obstacle.x = self.location.x + distance_left       # bereken afstand vanaf robot tot uitgelezen sensor
            # self.obstacle.y = self.location.y                       # obstacle staat op zelfde hoogte als robot
            # print(f"robot.x = {self.location.x}", f"robot.y = {self.location.y}", f"obstakel.x = {self.obstacle.x} ", f"obstakel.y = {self.obstacle.y}" )
            # map.map[int(self.obstacle.y)][int(self.obstacle.x)] = 255         # map de sensor lezing links
            # self.obstacle.x = self.location.x - distance_right      # bereken obstacle afstand rechts
            # map.map[int(self.obstacle.y)][int(self.obstacle.x)] = 255         # map obstacle afstand rechts
            # if self.total_distance_travelled_90 > 45 and self.total_distance_travelled_90 < 55:
            #     map.map[int(self.location.y)][int(self.location.x)] = 100
            # self.orientatie_last = 0
        if self.orientatie == 90:

            if self.orientatie_last != 90: #check of laatste orientatie richting anders was.
                x = reciever.unpack()
                self.distance_till_end = x[0]
                self.total_distance_travelled_90 = 0

            distance_travelled = self.distance_till_end - distance_front
            self.total_distance_travelled_90 = self.total_distance_travelled_90 + distance_travelled
            self.location.y = self.location.y
            self.location.x = self.location.x + distance_travelled
            self.obstacle.x = self.location.x
            self.obstacle.y = self.location.y - distance_left
            print(f"robot.x = {self.location.x}", f"robot.y = {self.location.y}", f"obstakel.x = {self.obstacle.x} ",
                  f"obstakel.y = {self.obstacle.y}")
            map.map[int(self.obstacle.y)][int(self.obstacle.x)] = 255
            self.obstacle.y = self.location.y + distance_right
            map.map[int(self.obstacle.y)][int(self.obstacle.x)] = 255
            if self.total_distance_travelled_90 > 45 and self.total_distance_travelled_90 < 55:
                map.map[int(self.location.y)][int(self.location.x)] = 155
            self.orientatie_last = 90

        if self.orientatie == 180:
            if self.orientatie_last != 180: #check of laatste orientatie richting anders was.
                self.distance_till_end = distance_front
                self.total_distance_travelled_180 = 0

            distance_travelled = self.distance_till_end - distance_front
            self.total_distance_travelled_180 = self.total_distance_travelled_180 + distance_travelled
            self.distance_till_end = distance_front
            self.location.y = self.location.y - distance_travelled  # bereken nieuwe y locatie in de map
            self.obstacle.x = self.location.x - distance_left  # bereken afstand vanaf robot tot uitgelezen sensor
            self.obstacle.y = self.location.y  # obstacle staat op zelfde hoogte als robot
            print(f"robot.x = {self.location.x}", f"robot.y = {self.location.y}", f"obstakel.x = {self.obstacle.x} ",
                  f"obstakel.y = {self.obstacle.y}")
            map.map[int(self.obstacle.y)][int(self.obstacle.x)] = 255  # map de sensor lezing links
            self.obstacle.x = self.location.x + distance_right  # bereken obstacle afstand rechts
            map.map[int(self.obstacle.y)][int(self.obstacle.x)] = 255  # map obstacle afstand rechts
            if self.total_distance_travelled_180 > 45 and self.total_distance_travelled_180 < 55:
                map.map[int(self.location.y)][int(self.location.x)] = 100
            self.orientatie_last = 90

        if self.orientatie == 270:
            if self.orientatie_last != 90:  # check of laatste orientatie richting anders was.
                x = reciever.unpack()
                self.distance_till_end = x[0]
                self.total_distance_travelled_270 = 0

            distance_travelled = self.distance_till_end - distance_front
            self.total_distance_travelled_270 = self.total_distance_travelled_270 + distance_travelled
            self.location.y = self.location.y
            self.location.x = self.location.x - distance_travelled
            self.obstacle.x = self.location.x
            self.obstacle.y = self.location.y + distance_left
            print(f"robot.x = {self.location.x}", f"robot.y = {self.location.y}", f"obstakel.x = {self.obstacle.x} ",
                  f"obstakel.y = {self.obstacle.y}")
            map.map[int(self.obstacle.y)][int(self.obstacle.x)] = 255
            self.obstacle.y = self.location.y - distance_right
            map.map[int(self.obstacle.y)][int(self.obstacle.x)] = 255
            if self.total_distance_travelled_270 > 45 and self.total_distance_travelled_270 < 55:
                map.map[int(self.location.y)][int(self.location.x)] = 100
            self.orientatie_last = 270


    def open_map(self):
        img = Image.fromarray(map.map)
        img.show()


if __name__ == '__main__':
    map = Map(150, 150)
    _mapMuren(map)
    UDP_receiver = UDP_receiver('192.168.203.128', 65000)  # pc ijdo, 192.168.55.128 mobiele hotspot ijdo
    reading = UDP_receiver.unpack()
    end_reading = reading[4]
    print(f'Distance_front: {reading[0]}', f'Distance_left:{reading[1]}', f'Distance_right: {reading[2]}' f'Odometry: {reading[3]}')
    dist_front = reading[0]
    dist_left = reading[1]
    dist_right = reading[2]
    maprobot = _mapRobot(map=map, dist_frnt=dist_front, dist_rght=dist_right, dist_lft=dist_left )

    while(int(reading[4])>0):
        reading = UDP_receiver.unpack()
        print(f'Distance_front: {reading[0]}', f'Distance_left:{reading[1]}',
              f'Distance_right: {reading[2]}' f'Odometry: {reading[3]}')
        dist_front = reading[0]
        dist_left = reading[1]
        dist_right = reading[2]
        odometry = reading[3]
        maprobot.update_robot(distance_left=dist_left, distance_right=dist_right, distance_front=dist_front, odometry=odometry, reciever=UDP_receiver)

    maprobot.open_map()


