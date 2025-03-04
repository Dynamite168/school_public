import socket, threading

def chatbot(client_soc):
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
        print(f'Message sent from {client_soc.getsockname()[0]}:')
        print('CLIENT WROTE: ' + msg.decode())

        client_soc.sendall(b'Received your message!\n')

listening_soc = socket.socket()
listening_soc.bind(('127.0.0.1', 12345))
listening_soc.listen()

while True:
    client_soc, addr = listening_soc.accept()
    threading.Thread(target=chatbot, args=(client_soc,)).start()