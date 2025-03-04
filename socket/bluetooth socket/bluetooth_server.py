import socket, threading
import bluetooth

def chatbot(client_soc, client_addr):
    while True:
        quitting = False
        # get message
        client_soc.sendall(b'Received your message!\n')
        msg = b''
        while b'\n' not in msg:
            msg += client_soc.recv(1024)

            if b'quit' in msg:
                client_soc.sendall('Thanks for using my server!'.encode())
                client_soc.close()
                quitting = True
                break
        if quitting:
            break
        print(f'Message sent from {client_addr}:')
        print('CLIENT WROTE: ' + msg.decode())

        client_soc.sendall(b'Received your message!\n')

listening_soc = socket.socket(family=socket.AF_BLUETOOTH, type=socket.SOCK_STREAM, proto=socket.BTPROTO_RFCOMM)
listening_soc.bind(('f4:ce:23:b2:ba:8c', 4))
listening_soc.listen()

while True:
    client_soc, addr = listening_soc.accept()
    client_name = bluetooth.lookup_name(addr[0])
    print(f'Connected to {client_name} at {addr[0]}')
    threading.Thread(target=chatbot, args=(client_soc,addr)).start()