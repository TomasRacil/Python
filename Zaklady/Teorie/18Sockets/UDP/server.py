#socket_echo_server_dgram.py
import socket
import sys

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print(f'starting up on {server_address[0]} port {server_address[1]}')
sock.bind(server_address)

while True:
    try:
        print('\nwaiting to receive message')
        data, address = sock.recvfrom(4096)

        print(f'received {len(data)} bytes from {address}')
        #print(data.decode('utf-8'))
        print(data.decode("utf-8"))
        if data:
            sent = sock.sendto(data, address)
            print(f'sent {sent} bytes back to {address}')
    except KeyboardInterrupt:
        break