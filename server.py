#coding= utf8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import socket
import thread

sockets = []

def deal(connection):
	while True:
		try:
			buf = connection.recv(1024)
			print buf
			for i in sockets:
				i.send(buf)
		except :
			break


if __name__ == '__main__':
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.bind(('localhost', 8001))
	sock.listen(5)
	while True:
		connection,address = sock.accept() 
		thread.start_new_thread(deal,(connection,))
		sockets.append(connection)

