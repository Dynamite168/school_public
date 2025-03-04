import socket
client_soc = socket.socket()

address = '127.0.0.1'
port = 12345
client_soc.connect((address, port))
print('Connected to: ' + str(address))
client_soc.sendall(b'Hello from client!')

while True:
    print('WAITING FOR SERVER...')
    data = client_soc.recv(1024)
    print('SERVER WROTE: ' + data.decode())
    send_data = input('INPUT CLIENT: ').encode()
    client_soc.sendall(send_data + b'\n')
    if 'quit' in send_data.decode():
        print('running')
        print('QUITTING...')
        print('WAITING FOR SERVER...')
        data = client_soc.recv(1024)
        print('SERVER WROTE: ' + data.decode())
        break