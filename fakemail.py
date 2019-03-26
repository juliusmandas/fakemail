#!/usr/bin/python3

import sys
import socket

if(len(sys.argv) != 5):
	print("Usage: ./fakemail.py <MAIL_SERVER> <FAKE_MAIL> <TARGET_MAIL> <\"MESSAGE\">")

else:
	HOST = sys.argv[1]
	FAKEMAIL = sys.argv[2]
	TARGET = sys.argv[3]
	MSG = sys.argv[4]

	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
	sock.connect((HOST, 25))
	print(sock.recv(256).decode("UTF-8"))

	sock.send(("HELO " + HOST + "\r\n").encode("UTF-8"))
	print(sock.recv(256).decode("UTF-8"))

	sock.send(("MAIL FROM: <"+ FAKEMAIL +">\r\n").encode("UTF-8"))
	print(sock.recv(256).decode("UTF-8"))

	sock.send(("RCPT TO: <"+ TARGET +">\r\n").encode("UTF-8"))
	print(sock.recv(256).decode("UTF-8"))

	sock.send(("DATA\r\n").encode("UTF-8"))
	print(sock.recv(256).decode("UTF-8"))

	sock.send(("FROM: " + FAKEMAIL[0:FAKEMAIL.find("@")] + " <" + FAKEMAIL + ">\r\nTo: <" + TARGET + ">\r\nSubject: " + TARGET[0:TARGET.find("@")] + "\r\n" + MSG +"\r\n.\r\n").encode("UTF-8"))
	print(sock.recv(256).decode("UTF-8"))
	sock.close()
