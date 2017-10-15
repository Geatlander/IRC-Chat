import socket
import _thread




s = socket.socket()
host = socket.gethostname()
print('host: ' + host)
port = 12345




s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('', port))



msg = "\nThank you for connecting"
user = input("Username: ")


def always_listen(threadname, delay):
	while msgsend != 'quit':
		received = ('\n'+c.recv(1024).decode())

		print(received)


def prompt():
	msgsend = user + ": " + input()
	c.sendto(msgsend.encode(), addr)

msgsend = ''

s.listen(5)
while True:
	c, addr = s.accept()
	print ('Got connection from', addr , '\n')
	c.sendto(msg.encode(), addr)

	_thread.start_new_thread(always_listen, ("Thread1", 2, ) )
	while msgsend != 'quit':
		prompt()
		
		


	c.close()
	print("closing the server down")		#close the connection









