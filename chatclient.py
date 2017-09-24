import socket
import _thread


s = socket.socket()
host = "192.168.1.191"
port = 12345

s.connect((host, port))

msg = ''

user = input("Username: ")


def toulisten(threadname, delay):
    while msg != 'quit':
        recu = ('\n'+s.recv(1024).decode())
        print(recu)


def prompt():
    msg = user + ": " + input()

    s.sendall(msg.encode())


_thread.start_new_thread(toulisten, ("Thread1", 2) )
while msg != 'quit':
    prompt()


print(s.recv(1024).decode())



s.close()
print("Logging off the client")




