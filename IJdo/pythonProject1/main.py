import socket
import sys
from struct import unpack

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
        return unpack('1f', message)





if __name__ == '__main__':
    UDP_receiver = UDP_receiver('192.168.178.178', 65000)
    # while True:
    x = UDP_receiver.unpack()
    print(f'Distance: {x}')
