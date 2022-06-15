from PIL import Image
import numpy as np

class data_point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class _mapRobot:
    def __init__(self):
        self.location = data_point(0,0) #robot start altijd in de hoek
        self.orientatie = 0
        self.map = np.zeros((300, 300), dtype=np.uint8)
        self.obstacle = data_point(0,0)

    def update_robot(self, distance_front, distance_left, distance_right, distance_traveld, odometry):# rechtdoor rijden, depth first algoritme.
        if odometry == 0:
            x_offset_right = 300 - distance_right # bereken locatie rechter sensor
            x_offset_left = 0 + distance_left # bereken locatie linker sensor
            x_offset_true = (x_offset_right + x_offset_left)/2 # pak het midden van de twee locaties.
            self.location.y = 300 - distance_front #elke keer dat de robot naar voren rijdt moet de update functie uitgevoerd worden.
        if odometry == 90:
            pass
            #doe iets.


        self.location.x = 0 + x_offset_true


        print(self.location.x)
        print(self.location.y)
        self.map[int(self.location.y)][int(self.location.x)] = 100
        self.map[int(self.location.y + (distance_front - 1))][int(self.location.x)] = 255
        self.map[int(self.location.y)][int(self.location.x + distance_right)] = 255
        self.map[int(self.location.y)][int(self.location.x - distance_left)] = 255

    # def update_obstacles(self, distance_front, distance_left, distance_right, distance_traveld, odometry):
    #     if odometry is 0:
    #
    #
    #     self.map[int(self.obstacle.y)][int(self.obstacle.y)] = 255

    def open_map(self):
        img = Image.fromarray(self.map)
        img.show()



class Mapper:
    def __init__(self):
        self.map = np.zeros((300,300))

    # def draw_map(self):

if __name__ == '__main__':
    maprobot = _mapRobot()
    for x in range(200):
        maprobot.update_robot((280 - x), 265, 25, 0, 0)

    maprobot.open_map()


