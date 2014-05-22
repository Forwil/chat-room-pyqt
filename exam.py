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
widget.setWindowTitle('Socket')

layout = QtGui.QGridLayout(widget)

text = QtGui.QTextBrowser()
lmessage = QtGui.QLabel("Message:")
message = QtGui.QLineEdit()
lname = QtGui.QLabel("Name:")
name = QtGui.QLineEdit()
name.setText("foo")
send = QtGui.QPushButton("Send")
send.setDisabled(True)

layout.addWidget(text,0,0,6,6)
layout.addWidget(lname,6,0)
layout.addWidget(name,6,1,1,2)
layout.addWidget(send,6,5,1,1)
layout.addWidget(lmessage,7,0,1,1)
layout.addWidget(message,7,1,1,5)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def sendfunc(sender):
	buf = name.text() + " :"+message.text() 
	message.clear()
	sock.send(unicode(buf))
	return

def network():
	while send.isEnabled() == False:
		try:
			sock.connect(('localhost', 8001))
		except:
			continue
		send.setDisabled(False)
	text.append("Connect success!\n")
	while True:
		try:
			ss = unicode(sock.recv(1024))
			print ss
			text.append("%s \n %s" % (time.asctime(),ss))
		except:
			pass
	thread.exit_thread()

send.mousePressEvent = sendfunc

widget.show()
thread.start_new_thread(network,())
app.exec_()
