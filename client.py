#coding =utf8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import thread
import socket
import time
from PyQt4 import QtGui
import PyQt4.Qt as Qt

app = QtGui.QApplication(sys.argv)

widget = QtGui.QWidget()
widget.resize(400, 300)
widget.setWindowTitle('Socket homework by 11091222')

layout = QtGui.QGridLayout(widget)

text = QtGui.QTextBrowser()
lmessage = QtGui.QLabel("Message:")
message = QtGui.QLineEdit()
lname = QtGui.QLabel("Name:")
name = QtGui.QLineEdit()
name.setText("foo")
send = QtGui.QPushButton("Send")
conn = QtGui.QPushButton("Conn")
send.setDisabled(True)

layout.addWidget(text,0,0,6,6)
layout.addWidget(lname,6,0)
layout.addWidget(name,6,1,1,2)
layout.addWidget(send,6,5,1,1)
layout.addWidget(conn,6,4,1,1)
layout.addWidget(lmessage,7,0,1,1)
layout.addWidget(message,7,1,1,5)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 8001
host = 'localhost'

def sendfunc(sender):
	if len(message.text())<=0:
		return 
	buf = name.text() + " :"+message.text() 
	message.clear()
	sock.send(unicode(buf))
	return

def connfunc(sender):
	global sock
	if send.isEnabled() == False:
		try:
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			sock.connect((host,port))	
			send.setDisabled(False)
			text.append("Connect success!")
			conn.setText("Exit")
		except:
			text.append("Connect fault!please check your network")
	else:
		send.setDisabled(True)
		sock.send("QUIT")
		sock.close()
		text.append("Connect close,Good-bye!")	
		conn.setText("Conn")
		

def recv():
	while True:
		try:
			ss = unicode(sock.recv(1024))
			print ss
			if len(ss)>1:
				text.append("%s \n %s" % (time.asctime(),ss))
		except:
			pass
	thread.exit_thread()

send.mousePressEvent = sendfunc
conn.mousePressEvent = connfunc

widget.show()
thread.start_new_thread(recv,())
app.exec_()
sys.exit(sock.close())
