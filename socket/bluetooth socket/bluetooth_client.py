import socket, bluetooth
client_soc = socket.socket(family=socket.AF_BLUETOOTH, type=socket.SOCK_STREAM, proto=socket.BTPROTO_RFCOMM)

address = "f4:ce:23:b2:ba:8c"
port = 4
print(bluetooth.lookup_name(address))
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
