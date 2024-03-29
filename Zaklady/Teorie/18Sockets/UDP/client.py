#socket_echo_client_dgram.py
import socket
import sys

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 10000)
message = b'This is the message.  It will be repeated.'

try:

    # Send data
    print(f'sending {message.decode("utf-8")}')
    sent = sock.sendto(message, server_address)

    # Receive response
    print('waiting to receive')
    data, server = sock.recvfrom(4096)
    print(f'received {data.decode("utf-8")}')
except KeyboardInterrupt:
    pass
finally:
    print('closing socket')
    sock.close()